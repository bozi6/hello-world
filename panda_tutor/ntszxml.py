from lxml import etree, objectify


def read_file_content(file_path):
    """Read the contents of a file and return them."""
    with open(file_path, 'r') as file:
        return file.read()


def process_layer(layer):
    """Print details of a layer and its children."""
    try:
        print(layer.index)
        for element in layer.getchildren():
            print(f"{element.attrib} => {element.text}")
    except AttributeError:
        pass


def parse_xml(xml_file):
    """Parse the XML file and process its contents."""
    xml_content = read_file_content(xml_file)
    root = objectify.fromstring(xml_content)

    # Print root attributes
    print("root.attrib", root.attrib)

    # Extract and print Layer and Fixture attributes
    try:
        layer_attrib = root.Layer.attrib
        fixture_attrib = root.Layer.Fixture.attrib
        print("Layer attributes: ", layer_attrib)
        print("Fixture attributes: ", fixture_attrib)
    except AttributeError:
        print("Error: Missing Layer or Fixture attributes")

    # Process each layer
    for layer in root.getchildren():
        process_layer(layer)


if __name__ == "__main__":
    xml_file_path = "ntsz_old.xml"
    parse_xml(xml_file_path)
