"""Ma2 layout Ma3 konvertálás."""
import maattribs

xml2 = maattribs.ma2attribs()
xml3 = maattribs.ma3attribs()
print(xml2.info['datetime'])
print(xml3.layout['Name'])
print(xml2.layoutdata['index'])
print(xml3.layout['Guid'])
xml2.layoutdata['index'] = 165
xml3.layout['Guid'] = 165
print(xml2.layoutdata['index'])
print(xml3.layout['Guid'])
print(xml2)

