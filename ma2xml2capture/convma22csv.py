import xml.etree.ElementTree as Xet
import pandas as pd

cols = ['Fixture', 'Optics', 'Wattage', 'Unit', 'Circuit', 'Channel',
        'Groups', 'Patch', 'DMX Mode', 'DMX Channles', 'Layer', 'Focus',
        'Filters', 'Gobos', 'Accessories', 'Purpose', 'Note', 'Weight',
        'Location', 'Position X', 'Position Y', 'Position Z', 'Rotation X',
        'Rotation Y', 'Rotation Z', 'Focus', 'Pan', 'Focus Tilt', 'Invert Pan',
        'Pan Start Limit', 'Pan End Limit', 'Invert Tilt', 'Tilt Start Limit',
        'Tilt End Limit', 'Identifier', 'External Identifier']

rows = []

# XML file feldogozása
xmlparse = Xet.parse("mindenki.xml")

root = xmlparse.getroot()
mv = root.attrib['major_vers']
miv = root.attrib['minor_vers']
sv = root.attrib['stream_vers']
print("Verzió: {}.{}.{}".format(mv, miv, sv))
# print(Xet.tostring(root, encoding='utf8').decode('utf8'))
for child in root:
    print("child tag: ", child.tag)
    print("child attrib: ", child.attrib)
    print(child.attrib["showfile"])
    for schild in child:
        print("subchild attr: ", schild.attrib)
        print("subchild tag: ", schild.tag)
        for lay in schild:
            print(lay.attrib)
            Fixture = lay.text
            rows.append({"Fixture": Fixture})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('kimenet.csv')
