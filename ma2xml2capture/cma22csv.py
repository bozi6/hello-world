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

# namespace definiálása az ma2 exportált xml alapján
ns = {'bas': "http://schemas.malighting.de/grandma2/xml/MA",
      'xsi': "http://www.w3.org/2001/XMLSchema-instance",
      'schema': "http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.9.60/MA.xsd"}

myroot = mytree.getroot()  # xml gyökér kijelölése itt <MA>
print('Showfile dátuma: {}'.format(myroot[0].attrib['datetime']))
print('Showfile neve: {}'.format(myroot[0].attrib['showfile']))
print("MA2 programverzió: {},{},{}".format(
    myroot.attrib['major_vers'], myroot.attrib['minor_vers'], myroot.attrib['stream_vers']))

# Alapváltozók amik nem vannak az exportált xmlben
op = '18°'
wa = '500W'
wg = "5,0kg"

for Layer in myroot[1].findall("bas:Layer", ns):
    extuid = uuid.uuid4()  # Kamu uuid generálása
    rn = Layer.attrib['name']  # Réteg nevének és indexének kinyerése
    ridx = Layer.attrib['index']
    for Fixture in Layer:
        fi = Fixture.attrib['index']  # Lámpa index és név
        fn = Fixture.attrib['name']
        #  Itt csak átalakítjuk a mostani fileban a macet gagyibbra lustaságból!
        if fn[:8] == 'Mac700PB':  # levágjuk a sorszámot a lámpanévből
            fn = 'Martin MAC 250 Entour'  # jól kicseréljük a capture student verzióval
        fdmx = Fixture[1][0][0].text  # Fixture/subfixture/patch szövege
        if fdmx != '0':  # ha nincs dmx címe a cuccnak akkor az előzőt adjuk a mdmxnek
            mdmx = fdmx
        fpos = Fixture[1][1][0].attrib  # Fixture/subfixture/absoluteposition/attribjai
        frot = Fixture[1][1][1].attrib
        if 'fixture_id' in Fixture.attrib:  # Ha robotlámpa akkor ma2 szerint fixture
            fixt_id = Fixture.attrib['fixture_id']
            op = "18,1°"
            wa = '326W'
            wg = "22,4kg"
        if 'channel_id' in Fixture.attrib:  # ha dimmer akkor channel ma2 szerint
            fixt_id = Fixture.attrib['channel_id']
            # A dimmerekből sima par64-et csinálunk !
            fn = 'Generic Par 64'
            op = 'CP63'
            wa = '1000W'
            wg = "1,8kg"
        if 'is_multipatch' in Fixture.attrib:  # ha multipatchelt a lámpa
            fdmx = mdmx
        data.append(
            [fn, op, wa, fn, '', fixt_id, ridx, fdmx, '', '', rn + " Layer", '', '', '', '', '', 'comment', wg, rn,
             fpos['x'] + 'm', fpos['y'] + 'm', fpos['z'] + 'm', frot['x'] + '°', frot['y'] + '°',
             frot['z'] + '°', '0°', '0°', 'No', '0°', '0°', 'No', '0°', '0°', 'No', '', extuid])

with open(kifile, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(fields)
    filewriter.writerows(data)
csvfile.close()
print("Az importálható cucc a {} -ban található.".format(kifile))
print("Ja amúgy kész vagyok...")
