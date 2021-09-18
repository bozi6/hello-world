import xml.sax


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
        if tag == "Fixture":
            fn = attributes["name"]
            self.Fixture = fn
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
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "Address":
            self.Address = content

    # Call when an elements ends


"""    def endElement(self, tag):
        print("End element: ", self.CurrentData)
        if self.CurrentData == "Fixture":
            print("Típus:", self.FixtureType)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        print("\tcharacters: ", self.CurrentData)
        if self.CurrentData == "Fixture":
            self.Fixture = content
        elif self.CurrentData == "Layer":
            self.Layer = content
        elif self.CurrentData == "Address":
            self.Address = content
        elif self.CurrentData == "Location":
            self.Location = content
        elif self.CurrentData == "Rotation":
            self.Rotation = content
        elif self.CurrentData == "Scaling":
            self.Scaling = content
"""

if __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default Contexthandler
    Handler = FixtureHandler()
    parser.setContentHandler(Handler)
    parser.parse("mindenki.xml")
