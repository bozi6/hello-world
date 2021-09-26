import xml.etree.ElementTree as Et
import csv
import uuid

befile = 'mindenki.xml'
kifile = befile + "_conv.csv"
# Ezek a mezők vannak a capture csv-ben
fields = (['Fixture', 'Optics', 'Wattage', 'Unit', 'Circuit', 'Channel',
           'Groups', 'Patch', 'DMX Mode', 'DMX Channles', 'Layer', 'Focus',
           'Filters', 'Gobos', 'Accessories', 'Purpose', 'Note', 'Weight',
           'Location', 'Position X', 'Position Y', 'Position Z', 'Rotation X',
           'Rotation Y', 'Rotation Z', 'Focus', 'Pan', 'Focus Tilt', 'Invert Pan',
           'Pan Start Limit', 'Pan End Limit', 'Invert Tilt', 'Tilt Start Limit',
           'Tilt End Limit', 'Identifier', 'External Identifier'])

data = []
mytree = Et.parse(befile)

ns = {'bas': "http://schemas.malighting.de/grandma2/xml/MA",
      'xsi': "http://www.w3.org/2001/XMLSchema-instance",
      'schema': "http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.9.60/MA.xsd"}

myroot = mytree.getroot()
print('Showfile dátuma: {}'.format(myroot[0].attrib['datetime']))
print('Showfile neve: {}'.format(myroot[0].attrib['showfile']))
print("MA2 programverzió: {},{},{}".format(
    myroot.attrib['major_vers'], myroot.attrib['minor_vers'], myroot.attrib['stream_vers']))

for Layer in myroot[1].findall("bas:Layer", ns):
    extuid = uuid.uuid4()
    rn = Layer.attrib['name']
    ridx = Layer.attrib['index']
    for Fixture in Layer:
        fi = Fixture.attrib['index']
        fn = Fixture.attrib['name']
        fdmx = Fixture[1][0][0].text  # Fixture/subfixture/patch szövege
        if fdmx != '0':
            mdmx = fdmx
        fpos = Fixture[1][1][0].attrib  # Fixture/subfixture/absoluteposition/attribjai
        frot = Fixture[1][1][1].attrib
        if 'fixture_id' in Fixture.attrib:
            fixt_id = Fixture.attrib['fixture_id']
        if 'channel_id' in Fixture.attrib:
            fixt_id = Fixture.attrib['channel_id']
        if 'is_multipatch' in Fixture.attrib:
            fdmx = mdmx
        data.append([fn, '', '', fn, '', fixt_id, ridx, fdmx, '', '', rn, '', '', '', '', '', 'comment', '', rn,
                     fpos['x'] + 'm', fpos['y'] + 'm', fpos['z'] + 'm', frot['x'] + '°', frot['y'] + '°',
                     frot['z'] + '°', '', '', '', '', '', ''
                                                          '', 'No', '', '', extuid])

with open(kifile, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(fields)
    filewriter.writerows(data)
csvfile.close()
print("Az importálható cucc a {} -ban található.".format(kifile))
print("Ja amúgy kész vagyok...")
