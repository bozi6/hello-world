import pandas as pd


# Encapsulate repeated separator logic
def display_message(message, empty_space=80):
    print("-" * empty_space)
    print(message.center(empty_space))
    print("-" * empty_space)


# Encapsulate Excel reading logic
def read_excel(file_path, sheet_name=None):
    return pd.read_excel(file_path, sheet_name=sheet_name)


# Encapsulate printing DataFrame column lists
def print_column_lists(data):
    if isinstance(data, pd.DataFrame):
        for column in data.columns:
            print(f"{column} oszlop: {data[column].to_list()}")
    elif isinstance(data, dict):
        # Iterate over all sheets if data is a dictionary
        for sheet_name, sheet_df in data.items():
            display_message(f"{sheet_name} oszlopai")
            print_column_lists(sheet_df)


# Main logic
if __name__ == "__main__":
    file_path = "test.xlsx"

    # Read the first worksheet and display its content
    df = read_excel(file_path)
    print(df)
    display_message("Táblázat oszlopaiból listák")
    print_column_lists(df)

    # Read a specific worksheet by index and display its content
    display_message("Második munkalap a táblázatból")
    df_sheet_index = read_excel(file_path, sheet_name=1)
    print(df_sheet_index)

    # Read a specific worksheet by name and display its content
    display_message("Munkalap név szerinti hivatkozással")
    df_sheet_by_name = read_excel(file_path, sheet_name="Lap1")
    print(df_sheet_by_name)

    # Read all worksheets and display their content with column lists
    display_message("Összes lap tartalma")
    all_sheets = read_excel(file_path, sheet_name=None)
    print_column_lists(all_sheets)  # Handles dictionary input

    # DataFrame creation and manipulation
    display_message("DataFrame példák")
    data = [["Axel", 32], ["Alíz", 26], ["Sanyi", 45]]
    df = pd.DataFrame(data, columns=["Név", "Kor"])
    print(df)

    # Print specific columns
    print("Név oszlop:", df["Név"])
    print("Kor oszlop:", df["Kor"])

    # Add a new column
    display_message("Új oszlop hozzáadása")
    example_column = pd.DataFrame([1, 2, 3], columns=["példa"])
    df["példa"] = example_column["példa"]
    print(df)

    # Remove a column
    display_message("Oszlop törlése")
    del df["példa"]
    print(df)

    # Select a specific row
    display_message("Egy sor kiválasztása")
    print(df.iloc[0])

    # Add a new row
    display_message("Új sor hozzáadása")
    new_user = pd.DataFrame([["Vivien", 33]], columns=["Név", "Kor"])
    df = pd.concat([df, new_user], ignore_index=True)
    print(df)
