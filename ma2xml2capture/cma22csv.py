import uuid
import xml.etree.ElementTree as Et
import csv
import lampak

input_dir = './xmlz/'
output_dir = './csvk/'
input_file = 'ntsz_old.xml'
input_path = input_dir + input_file
output_path = output_dir + input_file + "_conv.csv"
# Ezek a mezők vannak a capture csv-ben
fields = ['Fixture', 'Optics', 'Wattage', 'Unit', 'Circuit', 'Channel',
          'Groups', 'Patch', 'DMX Mode', 'DMX Channles', 'Layer', 'Focus',
          'Filters', 'Gobos', 'Accessories', 'Purpose', 'Note', 'Weight',
          'Location', 'Position X', 'Position Y', 'Position Z', 'Rotation X',
          'Rotation Y', 'Rotation Z', 'Focus', 'Pan', 'Focus Tilt', 'Invert Pan',
          'Pan Start Limit', 'Pan End Limit', 'Invert Tilt', 'Tilt Start Limit',
          'Tilt End Limit', 'Identifier', 'External Identifier']

data = []
mytree = Et.parse(input_path)

# namespace definiálása az ma2 exportált xml alapján
namespace = {'bas': "http://schemas.malighting.de/grandma2/xml/MA",
      'xsi': "http://www.w3.org/2001/XMLSchema-instance",
      'schema': "http://schemas.malighting.de/grandma2/xml/MA http://schemas.malighting.de/grandma2/xml/3.9.60/MA.xsd"}

myroot = mytree.getroot()  # xml gyökér kijelölése itt <MA>
print('Showfile dátuma: {}'.format(myroot[0].attrib['datetime']))
print('Showfile neve: {}'.format(myroot[0].attrib['showfile']))
print("MA2 programverzió: {},{},{}".format(
    myroot.attrib['major_vers'], myroot.attrib['minor_vers'], myroot.attrib['stream_vers']))

for Layer in myroot.findall("bas:Layer", namespace):
    layer_name = Layer.attrib['name']  # Réteg nevének és indexének kinyerése
    ridx = Layer.attrib['index']
    uid = uuid.uuid4()
    for Fixture in Layer:  # Lámpákon szaladunk végig.
        onefixture = lampak.Lampa(Fixture[0].attrib['name'])
        onefixture.Unit = Fixture.attrib['name']
        onefixture.Layer = layer_name
        onefixture.extidentifier = uid
        fixture_index = Fixture.attrib['index']  # Lámpa index és név
        ''''#  Itt csak átalakítjuk a mostani fileban a macet gagyibbra lustaságból!
        if egylampa.Fixture[:8] == 'Mac700PB':  # levágjuk a sorszámot a lámpanévből
            egylampa.Fixture = 'Martin MAC 250 Entour'  # jól kicseréljük a capture student verzióval
        '''
        onefixture.Patch = Fixture[1][0][0].text  # Fixture/subfixture/patch szövege
        if onefixture.Patch != '0':  # ha nincs dmx címe a cuccnak akkor az előzőt adjuk a mdmxnek
            mdmx = onefixture.Patch
        fpos = Fixture[1][1][0].attrib  # Fixture/subfixture/absoluteposition/attribjai
        onefixture.posx = fpos['x'] + 'm'
        onefixture.posy = fpos['y'] + 'm'
        onefixture.posz = fpos['z'] + 'm'
        frot = Fixture[1][1][1].attrib
        onefixture.rotx = frot['x'] + '°'
        onefixture.roty = frot['y'] + '°'
        onefixture.rotz = frot['z'] + '°'
        if 'fixture_id' in Fixture.attrib:  # Ha robotlámpa akkor ma2 szerint fixture
            onefixture.Channel = Fixture.attrib['fixture_id']
        if 'channel_id' in Fixture.attrib:  # ha dimmer akkor channel ma2 szerint
            onefixture.Channel = Fixture.attrib['channel_id']
        if 'is_multipatch' in Fixture.attrib:  # ha multipatchelt a lámpa
            onefixture.Patch = mdmx

        data.append(onefixture.lamplista())


with open(output_path, 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(fields)
    filewriter.writerows(data)

csvfile.close()
print("Az importálható cucc a {} -ban található.".format(output_path))
print("Ja amúgy kész vagyok...")
