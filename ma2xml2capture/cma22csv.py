import uuid
import xml.etree.ElementTree as Et
import csv
from ma2xml2capture.lampak.lampa import Lampa as La

befile = 'teruletisebzes.xml'
kifile = befile + "_conv.csv"
# Ezek a mezők vannak a capture csv-ben
fields = ['Fixture', 'Optics', 'Wattage', 'Unit', 'Circuit', 'Channel',
          'Groups', 'Patch', 'DMX Mode', 'DMX Channles', 'Layer', 'Focus',
          'Filters', 'Gobos', 'Accessories', 'Purpose', 'Note', 'Weight',
          'Location', 'Position X', 'Position Y', 'Position Z', 'Rotation X',
          'Rotation Y', 'Rotation Z', 'Focus', 'Pan', 'Focus Tilt', 'Invert Pan',
          'Pan Start Limit', 'Pan End Limit', 'Invert Tilt', 'Tilt Start Limit',
          'Tilt End Limit', 'Identifier', 'External Identifier']

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

for Layer in myroot.findall("bas:Layer", ns):
    rn = Layer.attrib['name']  # Réteg nevének és indexének kinyerése
    ridx = Layer.attrib['index']
    uid = uuid.uuid4()
    for Fixture in Layer:  # Lámpákon szaladunk végig.
        egylampa = La(Fixture.attrib['name'])
        egylampa.Layer = rn
        egylampa.Identifier = uid
        fi = Fixture.attrib['index']  # Lámpa index és név
        #  Itt csak átalakítjuk a mostani fileban a macet gagyibbra lustaságból!
        '''if egylampa.Fixture[:8] == 'Mac700PB':  # levágjuk a sorszámot a lámpanévből
            egylampa.Fixture = 'Martin MAC 250 Entour'  # jól kicseréljük a capture student verzióval
        '''
        egylampa.Patch = Fixture[1][0][0].text  # Fixture/subfixture/patch szövege
        if egylampa.Patch != '0':  # ha nincs dmx címe a cuccnak akkor az előzőt adjuk a mdmxnek
            mdmx = egylampa.Patch
        fpos = Fixture[1][1][0].attrib  # Fixture/subfixture/absoluteposition/attribjai
        egylampa.posx = fpos['x']+'m'
        egylampa.posy = fpos['y']+'m'
        egylampa.posz = fpos['z']+'m'
        frot = Fixture[1][1][1].attrib
        egylampa.rotx = frot['x']+'°'
        egylampa.roty = frot['y']+'°'
        egylampa.rotz = frot['z']+'°'
        if 'fixture_id' in Fixture.attrib:  # Ha robotlámpa akkor ma2 szerint fixture
            egylampa.Channel = Fixture.attrib['fixture_id']
            '''
            egylampa.Optics = "18,1°"
            egylampa.Wattage = '326W'
            egylampa.Weight = "22,4kg"
            '''
        if 'channel_id' in Fixture.attrib:  # ha dimmer akkor channel ma2 szerint
            egylampa.Channel = Fixture.attrib['channel_id']
            if Fixture.attrib['name'][:3] == "Dim":
                import lampak.par64
                parcan = lampak.par64.Par_64()
                egylampa.Fixture = parcan.Fixture
                egylampa.Optics = parcan.Optics
                egylampa.Weight = parcan.Weight
                egylampa.Wattage = parcan.Wattage
            '''# A dimmerekből sima par64-et csinálunk !
            egylampa.Name = 'Generic Par 64'
            egylampa.Optics = 'CP63'
            egylampa.Wattage = '1000W'
            egylampa.Weight = "1,8kg"'''
        if 'is_multipatch' in Fixture.attrib:  # ha multipatchelt a lámpa
            egylampa.Patch = mdmx

        data.append(egylampa.lamplista())

'''
for Layer in myroot.findall("bas:Layer", ns):
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
'''

with open(kifile, 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(fields)
    filewriter.writerows(data)

csvfile.close()
print("Az importálható cucc a {} -ban található.".format(kifile))
print("Ja amúgy kész vagyok...")