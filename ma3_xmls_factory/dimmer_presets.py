import random
import string

import xml.etree.ElementTree as ett


class CreatePresets(object):
    def __init__(self):
        self.kimeneti_mappa = "/Users/mnte/MALightingTechnology/gma3_library/datapools/macros/"
        self.ertekek = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
        self.tree = ett.ElementTree
        self.create_macro()

    @staticmethod
    def uidgen():
        szoveg = "".join([random.choice(string.hexdigits[:16]) for x in range(32)])
        uid = ' '.join(szoveg[i:i + 2] for i in range(0, len(szoveg), 2))
        return uid.upper()

    def create_macro(self):
        """
        Creates the macro file
        """
        kimeneti_file = "dimmer presets.xml"

        root = ett.Element("GMA3")
        root.set("DataVersion", "1.8.1.0")

        macro = ett.SubElement(root, "Macro")
        macro.set("Name", "Dimmer Presets")
        macro.set("Guid", self.uidgen())

        for i in range(1, 12):
            macroline = ett.SubElement(macro, "MacroLine")
            macroline.set("Command", "Fixture 1 At {}".format(self.ertekek[i - 1]))
            macroline = ett.SubElement(macro, "MacroLine")
            macroline.set("Command", "Store Preset 1.{}".format(i))
            macroline = ett.SubElement(macro, "MacroLine")
            macroline.set("Command", "Label Preset 1.{} \"{}%\"".format(i, self.ertekek[i - 1]))

        self.tree = ett.ElementTree(root)
        ett.indent(self.tree)
        self.write_xml_file(self.kimeneti_mappa + kimeneti_file)

    def write_xml_file(self, output_file):
        with open(output_file, "wb") as files:
            self.tree.write(files, xml_declaration=True, encoding="UTF-8", method="xml")


if __name__ == "__main__":
    newdim = CreatePresets()
    print("Dimmer preset xml file created.")
