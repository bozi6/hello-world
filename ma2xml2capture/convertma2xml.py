import xml.sax
import csv


class FixtureHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.Info = ""
        self.Layers = ""
        self.Layer = ""
        self.Fixture = ""
        self.FixtureType = ""
        self.Optics = ""
        self.Wattage = ""
        self.Unit = ""
        self.Circuit = ""
        self.Channel = ""
        self.Groups = ""
        self.Patch = ""
        self.DMX_Mode = ""
        self.DMX_Channels = ""
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
        self.Focus = ""
        self.Filters = ""
        self.Gobos = ""
        self.Accessories = ""
        self.Purpose = ""
        self.Note = ""
        self.Weight = ""
        self.focuspan = ""
        self.foctilt = ""
        self.ip = ""
        self.psl = ""
        self.pel = ""
        self.it = ""
        self.tsl = ""
        self.tel = ""
        self.ident = ""
        self.xid = ""
        self.cucc = []

    # Call when element starts
    def startElement(self, tag, attributes):
        #  print("StartElement: ", self.CurrentData)
        self.CurrentData = tag
        if tag == "Info":
            datum = attributes["datetime"]
            showfile = attributes["showfile"]
            self.Info = "Showfile neve:" + showfile + " - Dátum:" + datum
        if tag == "Layers":
            lsz = attributes["index"]
            self.Layers = lsz
        if tag == "Layer":
            nev = attributes["name"]
            self.Layer = nev
            self.Groups = nev
        if tag == "FixtureType":
            if attributes["name"][2:] == "Dimmer 00":
                self.FixtureType = "Generic Par 64"
                self.Optics = "CP63"
                self.Wattage = "1000W"
            else:
                self.FixtureType = attributes["name"][2:]
        if tag == "Fixture":
            fn = attributes["name"]
            self.Fixture = fn
            self.Unit = fn
        if tag == "Location":
            self.px = attributes["x"]
            self.py = attributes["y"]
            self.pz = attributes["z"]
        if tag == "Rotation":
            self.rx = attributes["x"]
            self.ry = attributes["y"]
            self.rz = attributes["z"]

    def endElement(self, tag):
        # Ismétlődés elkerülésére kell
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "Address":
            self.Address = content

    def mimegy(self):
        if self.Fixture != "" and self.ident != "":
            self.cucc.append([self.Fixture, self.Optics, self.Wattage, self.Unit, self.Circuit,
                              self.Channel, self.Groups, self.Patch, self.DMX_Mode, self.DMX_Channels,
                              self.Layer, self.Focus, self.Filters, self.Gobos, self.Accessories,
                              self.Purpose, self.Note, self.Weight, self.Location, self.px,
                              self.py, self.pz, self.rx, self.ry, self.rz, self.focuspan, self.foctilt,
                              self.ip, self.psl, self.pel, self.it, self.tsl, self.tel, self.ident, self.xid])


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
        filewriter.writerow(Handler.cucc)
        print(Handler.mimegy())
    csvfile.close()
