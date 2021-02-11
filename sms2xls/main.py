from xml.dom import minidom
import re
# parse xml file by name

mydoc = minidom.parse('sms.xml')

items = mydoc.getElementsByTagName('sms')

# one specific item attribute
print('Item #2 attribute:')
print(items[1].attributes['body'].value)

# all item attributes
print('\nAll attributes:')
for elem in items:
    tel = elem.attributes['address'].value
    if tel == '+36309400700':
        rd = elem.attributes['readable_date'].value
        bd = elem.attributes['body'].value
        pattern = r"\+|\-[\d]*.*,?-?HUF;"
        x = re.search(pattern, bd).group()
        print('Dátum: {} - Üzi: {}'.format(rd, bd))
        print(x)
print()

# one specific item's data
""" print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild)
"""