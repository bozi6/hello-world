import pandas as pd


def sor():
    print("-" * 80)


df = pd.read_excel('test.xlsx')
print(df)
sor()
print(df["A"].to_list())
print(df["B"].to_list())
print(df["C"].to_list())

#  lap megadása index szerint: 0 -az első
df_sheet_index = pd.read_excel('test.xlsx', sheet_name=1)
print(df_sheet_index)
#  lap megadás laapnév szerint:
df_sheet_index = pd.read_excel('test.xlsx', sheet_name='Lap1')
print(df_sheet_index)
#  összes lap megadása
df_sheet_all = pd.read_excel('test.xlsx', sheet_name=None)
sor()
print(df_sheet_all['Lap1'])
sor()
print(df_sheet_all['Lap2'])
sor()
print("Most valami teljesen más")
data = [['Axel', 32], ['Alíz', 26], ['Sanyi', 45]]
df = pd.DataFrame(data, columns=['Név', 'Kor'])
print(df)
sor()
print(df["Név"])
print(df["Kor"])
#  Új oszlop hozzáadása
sor()
c = pd.DataFrame([1, 2, 3], columns=["példa"])
df["példa"] = c["példa"]
print(df)
#  egy oszlop törlése
del df["példa"]
print(df)
#  egy sor kiválasztása
print(df.iloc[0])
# új sor hozzáadása
user = pd.DataFrame([['Vivien', 33]], columns=['Név', 'Kor'])
df = pd.concat([df, user])
print(df)
