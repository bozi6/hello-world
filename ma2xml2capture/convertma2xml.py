import xml.sax
import csv


class FixtureHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        super().__init__()
        self.CurrentData = ""
        self.Info = ""
        self.Layers = ""
        self.Layer = ""
        self.Fixture = ""
        self.FixtureType = ""
        self.Location = ""
        self.Rotation = ""
        self.Scaling = ""
        self.px = ""
        self.py = ""
        self.pz = ""
        self.rx = ""
        self.ry = ""
        self.rz = ""
        self.Address = ""
        self.cucc = []

    # Call when element starts
    def startElement(self, tag, attributes):
        #  print("StartElement: ", self.CurrentData)
        self.CurrentData = tag
        if tag == "Info":
            print("Információk:")
            datum = attributes["datetime"]
            showfile = attributes["showfile"]
            print("Showfile neve: {} - Dátum: {}".format(showfile, datum))
        if tag == "Layers":
            lsz = attributes["index"]
            self.Layers = lsz
            print("Rétegek száma: ", lsz)
        if tag == "Layer":
            nev = attributes["name"]
            print("Réteg neve: ", nev)
            self.Layer = nev
        if tag == "FixtureType":
            if attributes["name"][2:] == "Dimmer 00":
                self.FixtureType = "Generic Par 64"
                self.cucc.append(self.FixtureType)
                self.cucc.append("CP63")
                self.cucc.append("1000W")
            else:
                self.FixtureType = attributes["name"][2:]
                self.cucc.append(self.FixtureType)
        if tag == "Fixture":
            fn = attributes["name"]
            self.Fixture = fn
            self.cucc.append(self.Fixture)
            print("Lámpa: ", fn)
        if tag == "Location":
            self.px = attributes["x"]
            self.py = attributes["y"]
            self.pz = attributes["z"]
            print("Hely: ", self.px, self.py, self.pz)
        if tag == "Rotation":
            self.rx = attributes["x"]
            self.ry = attributes["y"]
            self.rz = attributes["z"]
            print("Forgatás: ", self.rx, self.ry, self.rz)


    def endElement(self, tag):
        if self.CurrentData == "Address":
            print("DMX cím:", self.Address)
        # Ismétlődés elkerülésére kell
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "Address":
            self.Address = content


if __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default Contexthandler
    Handler = FixtureHandler()
    parser.setContentHandler(Handler)
    parser.parse("mindenki.xml")
    cucc = Handler.cucc
    # Ezek a mezők vannak a capture csv-ben
    fields = (['Fixture', 'Optics', 'Wattage', 'Unit', 'Circuit', 'Channel',
               'Groups', 'Patch', 'DMX Mode', 'DMX Channles', 'Layer', 'Focus',
               'Filters', 'Gobos', 'Accessories', 'Purpose', 'Note', 'Weight',
               'Location', 'Position X', 'Position Y', 'Position Z', 'Rotation X',
               'Rotation Y', 'Rotation Z', 'Focus', 'Pan', 'Focus Tilt', 'Invert Pan',
               'Pan Start Limit', 'Pan End Limit', 'Invert Tilt', 'Tilt Start Limit',
               'Tilt End Limit', 'Identifier', 'External Identifier'])

    with open('mindenki_conv.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(fields)
        filewriter.writerow([Handler.cucc])
    csvfile.close()
