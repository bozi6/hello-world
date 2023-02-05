from lxml import etree, objectify


def parseXML(xmlFile):
    """Parse the XML file"""
    with open(xmlFile) as f:
        xml = f.read()

    root = objectify.fromstring(xml)

    # return attributes in element noda as dict
    attrib = root.attrib
    print("root.attrib", attrib)
    # how to extract element data
    begin = root.Layer.attrib
    uid = root.Layer.Fixture.attrib
    print("begin: ", begin)
    print("uid: ", uid)
    # loop over elements and print their tags and text
    for layer in root.getchildren():
        try:
            print(layer.index)
            for e in layer.getchildren():
                print("{} => {}".format(e.attrib, e.text))
        except AttributeError:
            pass
    print()

    """
    # How to add a new element
    root.appointment.new_element = "new data"
    
    # Remove the py:pytype stuff
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True)
    print(obj_xml)

    # save your xml
    with open("new.xml", "wb") as f:
        f.write(obj_xml)
    """


if __name__ == "__main__":
    f = 'ntsz_old.xml'
    parseXML(f)

