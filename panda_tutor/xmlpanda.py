from lxml import objectify
import pandas as pd

XML_FILE_PATH = "../ma2xml2capture/xmlz/ntsz_old.xml"


def parse_xml_to_dataframe(file_path):
    """Parse XML file and convert it to a Pandas DataFrame."""
    xml_data = objectify.parse(file_path)
    root = xml_data.getroot()

    children = root.getchildren()
    row_data = [[subchild.text for subchild in child.getchildren()] for child in children]
    column_tags = [child.tag for child in children]

    df = pd.DataFrame(row_data).T
    df.columns = column_tags
    return df


if __name__ == "__main__":
    dataframe = parse_xml_to_dataframe(XML_FILE_PATH)
    print(dataframe)
