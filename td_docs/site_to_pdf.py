import os
import asyncio
from playwright.async_api import async_playwright
from pypdf import PdfWriter, PdfReader

ROOT = "./httpdocs"
PDF_DIR = "./pdf_pages"
OUTPUT = "complete_site.pdf"

os.makedirs(PDF_DIR, exist_ok=True)

html_files = []

for root, dirs, files in os.walk(ROOT):
    for f in files:
        if f.endswith(".htm") or f.endswith(".html"):
            html_files.append(os.path.join(root, f))

html_files.sort()


async def render_pdfs():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for i, file in enumerate(html_files):
            path = "file://" + os.path.abspath(file)

            print(f"{i+1}/{len(html_files)} -> {file}")

            try:
                await page.goto(path, wait_until="networkidle")
                pdf_path = os.path.join(PDF_DIR, f"{i:05d}.pdf")

                await page.pdf(
                    path=pdf_path,
                    format="A4",
                    print_background=True
                )

            except Exception as e:
                print("error:", e)

        await browser.close()


asyncio.run(render_pdfs())

print("PDF pages ready. Merging...")

writer = PdfWriter()

for f in sorted(os.listdir(PDF_DIR)):
    if f.endswith(".pdf"):
        reader = PdfReader(os.path.join(PDF_DIR, f))
        for page in reader.pages:
            writer.add_page(page)

with open(OUTPUT, "wb") as out:
    writer.write(out)

print("DONE ->", OUTPUT)

