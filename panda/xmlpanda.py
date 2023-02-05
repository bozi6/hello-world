from lxml import objectify
import pandas as pd

xml_data = objectify.parse('../ma2xml2capture/xmlz/ntsz_old.xml')
root = xml_data.getroot()

data = []
cols = []
for i in range(len(root.getchildren())):
    child = root.getchildren()[i]
    data.append([subchild.text for subchild in child.getchildren()])
    cols.append(child.tag)

df = pd.DataFrame(data).T
print(df)
df.columns = cols
print(df)
