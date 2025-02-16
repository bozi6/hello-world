#  payment_receipts.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY;.
#      This is free software, and you are welcome to redistribute it.
#   Last Modified: 2023. 12. 19. 10:12

# import modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import payment_receipts_data

# creating a Base Document Template of page size a4
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# fetching the style of Top level heading (Heading)
title_style = styles["Heading1"]

# 0: left, 1: center, 2:right
title_style.aligment = 1


# Creating the paragraph with
# the heading text and parsing the styles of it
title = Paragraph(payment_receipts_data.HEADER, title_style)

# creates a Table Style object and in it,
# defines the styles row wise
# the tuples which look like coordinates
# are nothing but rows and columns
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("BACKGROUND", (0, 4), (3, 4), colors.chartreuse),
    ]
)

# creates a table object and passes the style to it
table = Table(payment_receipts_data.DATA, style=style)

# final step which builds the
# actual pdf putting together all the elements
pdf.build([title, table])
