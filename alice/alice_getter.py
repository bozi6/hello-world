from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import textwrap

"""
Alice csodaországban letöltő 
segédprogram a mek.oszk.hu oldalról
"""


def tag_visible(element):
    """
    Megnézhető e a htmlben lévő tag
    :param element: a keresett elem
    :return: False ha a szülő elem neve benne van a listában és True
    """
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    """
    Szöveget készít HTML-ből
    :param body: A html szövege
    :return: Sima olvasható szöveg.
    """
    soup = BeautifulSoup(body, "html.parser")
    texts = soup.find_all(string=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)


def main():
    """
    Főprogram Alice letöltésére
    :return:
    """
    html = urllib.request.urlopen(
        "https://mek.oszk.hu/00300/00348/html/alice01.htm"
    ).read()
    print(textwrap.fill(text_from_html(html), 80))

    f = open("alice_csodaorszagban.txt", "a")
    tordelt = textwrap.fill(text_from_html(html), 80)
    f.write(tordelt)
    f.write("\n")
    f.write("-" * 80)


if __name__ == "__main__":
    main()
