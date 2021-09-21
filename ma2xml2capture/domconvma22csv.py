from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse('mindenki.xml')
collection = DOMTree.documentElement
mv = collection.getAttribute('major_vers')
miv = collection.getAttribute('minor_vers')
sv = collection.getAttribute('stream_vers')
print("Verzió: {}.{}.{}".format(mv, miv, sv))

# get all the fixtures in the collection
Lnum = collection.getElementsByTagName("Layers")
Layers = collection.getElementsByTagName("Layer")
print("Rétegek száma: ", Lnum[0].getAttribute('index'))
for Layer in Layers:
        Fixture = Layer.getElementsByTagName('Fixture')
        Patch = Layer.getElementsByTagName('Address')
        # todo megoldani a cuccokhoz a hozzáférést mert nem megy.
        ABSPosition = Layer.getElementsByTagName('AbsolutePosition')
        print("Lámpa neve: ", Fixture[0].getAttribute('name'))
        print("Cím: ", Patch[0].firstChild.data)
        for loca in ABSPosition.iter('Location'):
                print(loca)

cols = ['Fixture', 'Optics', 'Wattage', 'Unit', 'Circuit', 'Channel',
        'Groups', 'Patch', 'DMX Mode', 'DMX Channles', 'Layer', 'Focus',
        'Filters', 'Gobos', 'Accessories', 'Purpose', 'Note', 'Weight',
        'Location', 'Position X', 'Position Y', 'Position Z', 'Rotation X',
        'Rotation Y', 'Rotation Z', 'Focus', 'Pan', 'Focus Tilt', 'Invert Pan',
        'Pan Start Limit', 'Pan End Limit', 'Invert Tilt', 'Tilt Start Limit',
        'Tilt End Limit', 'Identifier', 'External Identifier']

rows = []

"""
# rows.append({"Layer": currentLayerName,
                "Fixture": currentFixture,
                "melyikcella": valtozoNev...
                })
"""

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('kimenet.csv')
