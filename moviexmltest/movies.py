import xml.etree.ElementTree as Et

tree = Et.parse('movies.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

input("gyerek elemek listázása")
for movie in root.iter('movie'):
    print(movie.attrib)

input("filmek attribútumai")
for description in root.iter('description'):
    print(description.text)
input("filmek leírása")
# search the tree for movies that came out in 1992:
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)
input("1992-es filmek listája")
# find movies that are available in multiple formats
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
input("multiformátumú filmek listázása")
# find movies that are available in multiple formats print the parent element
# with ...
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)
input("multiformátum szülő lista")
# Egy elem megkeresése és cserélése
b2tf = root.find("./genre/decade/movie/[@title='Back 2 the Future']")
print(b2tf)
b2tf.attrib['title'] = "Back to the Future"
print(b2tf.attrib)
input("Back2thefuture javítása")
"""
# Fájl kiírása vissza és a javított dolog elhelyezése
tree.write("movies.xml")

# Ismételt kiírás ellenőrzésileg
tree.Et.parse('movies.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)
"""

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
input("multiformat kiirása")
# A movie format multiple javítása csak Yes vagy No-ra
"""
import re

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')

# Write out the tree to the file again
tree.write("movies.xml")

tree = ET.parse('movies.xml')
root = tree.getroot()

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
"""

# Évtized és évek kiírása
for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')
input("Évtizedek és évek kiirása")
# milyen filmek vannak 2000 ből
for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)
input("Flimek listázása 2000ből")
# Új évtized hozzáadása az akciófilmek kategóriához
action = root.find("./genre[@category='Action']")
new_dec = Et.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

print(Et.tostring(action, encoding='utf8').decode('utf8'))
input("Új kategória hozzáadva")
# márcsak átrakjuk az X-ment a 90-esből a 2000-es évtizedbe
xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

print(Et.tostring(action, encoding='utf8').decode('utf8'))
input("Csere megtörtént")
