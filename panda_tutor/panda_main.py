import pandas as pd


if __name__ == "__main__":

    def sor(uzi):
        emptyspace = 80
        print("-" * emptyspace)
        print(uzi.center(emptyspace))
        print("-" * emptyspace)

    df = pd.read_excel("test.xlsx")
    print(df)
    sor("Táblázat oszlopaiból listák")
    print("A oszlop: ", df["A"].to_list())
    print("B oszlop: ", df["B"].to_list())
    print("C oszlop: ", df["C"].to_list())

    #  lap megadása index szerint: 0 -az első
    sor("Második munkalap a táblázatból:")
    df_sheet_index = pd.read_excel("test.xlsx", sheet_name=1)
    print(df_sheet_index)
    #  lap megadás lapnév szerint:
    sor("Munkalap név szerinti hivatkozással")
    df_sheet_index = pd.read_excel("test.xlsx", sheet_name="Lap1")
    print(df_sheet_index)
    #  összes lap megadása
    df_sheet_all = pd.read_excel("test.xlsx", sheet_name=None)
    sor("Összes lap után")
    sor("Első lap")
    print(df_sheet_all["Lap1"])
    sor("Második lap")
    print(df_sheet_all["Lap2"])
    print("Most valami teljesen más")
    data = [["Axel", 32], ["Alíz", 26], ["Sanyi", 45]]
    df = pd.DataFrame(data, columns=["Név", "Kor"])
    sor("Data frameból kiiratás")
    print(df)
    print(df["Név"])
    print(df["Kor"])
    #  Új oszlop hozzáadása
    sor("Új oszlop hozzáadása")
    c = pd.DataFrame([1, 2, 3], columns=["példa"])
    df["példa"] = c["példa"]
    print(df)
    sor("Ņszlop törlése")
    #  egy oszlop törlése
    del df["példa"]
    print(df)
    #  egy sor kiválasztása
    sor("Egy sor kiválasztása")
    print(df.iloc[0])
    # új sor hozzáadása
    user = pd.DataFrame([["Vivien", 33]], columns=["Név", "Kor"])
    df = pd.concat([df, user])
    sor("Új sor hozzáadva")
    print(df)
