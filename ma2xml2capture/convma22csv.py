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
# Namespaces declarations
ns = {'base': 'http://schemas.malighting.de/grandma2/xml/MA',
      'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
      'xsi-schema': 'http://schemas.malighting.de/grandma2/xml/MA '
                    'http://schemas.malighting.de/grandma2/xml/3.9.60/MA.xsd'
      }
root = xmlparse.getroot()

mv = root.attrib['major_vers']
miv = root.attrib['minor_vers']
sv = root.attrib['stream_vers']
print("Verzió: {}.{}.{}".format(mv, miv, sv))
# print(Xet.tostring(root, encoding='utf8').decode('utf8'))
for fixture in root.findall('base:Layers/base:Layer/base:Fixture/[@name]', ns):
    for adatz in fixture.findall('base:SubFixture/base:AbsolutePosition', ns):
        print(adatz.items())
        print('Eszköznév: ', fixture.attrib['name'])
        if 'fixture_id' in fixture.attrib:
            print('Lámpaazonosító: ', fixture.attrib['fixture_id'])
        elif 'channel_id' in fixture.attrib:
            print('Csatornaazonosító: ', fixture.attrib['channel_id'])
        print("DMX cím: ", adatz.text)
""" Ez volt a fasza
    for adatz in fixture.findall('base:SubFixture/base:Patch/base:Address', ns):
        print('Eszköznév: ', fixture.attrib['name'])
        if 'fixture_id' in fixture.attrib:
            print('Lámpaazonosító: ', fixture.attrib['fixture_id'])
        elif 'channel_id' in fixture.attrib:
            print('Csatornaazonosító: ', fixture.attrib['channel_id'])
        print("DMX cím: ", adatz.text)
"""
# rows.insert({"Layer": currentLayerName})


df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('kimenet.csv')
