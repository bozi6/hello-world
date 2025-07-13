import pandas as pd

SEPARATOR_LENGTH = 80


def print_separator(message):
    """Print a separator with a centered message."""
    print("-" * SEPARATOR_LENGTH)
    print(message.center(SEPARATOR_LENGTH))
    print("-" * SEPARATOR_LENGTH)


def display_dataframe(df, title):
    """Helper to display and label output for any DataFrame."""
    print_separator(title)
    print(df)


def pandas_intro():
    """Demonstrates basic Pandas usage."""
    # Basic DataFrame example
    dataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
    df = pd.DataFrame(dataset)
    display_dataframe(df, "Dataset Display")

    # Pandas version information
    print_separator("Pandas Version")
    print(f"Pandas Version: {pd.__version__}")

    # Pandas Series example
    series_example = [1, 7, 2]
    series = pd.Series(series_example)
    display_dataframe(series, "Series Example")
    print_separator("First Element of Series")
    print(series[0])

    # Series with custom index
    custom_index_series = pd.Series(series_example, index=["x", "y", "z"])
    display_dataframe(custom_index_series, "Custom-Index Series")
    print_separator("Access by Label")
    print(custom_index_series["y"])

    # Series from dictionary
    calories = {"day1": 420, "day2": 300, "day3": 390}
    dict_series = pd.Series(calories)
    display_dataframe(dict_series, "Series from Dictionary")

    # Partial series
    partial_series = pd.Series(calories, index=["day1", "day2"])
    display_dataframe(partial_series, "Partial Series")

    # DataFrame example with 2D data
    data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
    df = pd.DataFrame(data)
    display_dataframe(df, "2D DataFrame Example")

    # Locating rows
    display_dataframe(df.loc[[0]], "First Row")
    display_dataframe(df.loc[[0, 1]], "First Two Rows")


def clean_and_inspect_csv(file_path="data.csv"):
    """Cleans, inspects, and displays essential information from a CSV."""
    df = pd.read_csv(file_path)
    display_dataframe(df.head(10), "First 10 Rows of CSV")

    print_separator("DataFrame Info")
    print(df.info())

    # Data cleaning examples
    print_separator("Drop Missing Values")
    df_cleaned = df.dropna()  # To modify in-place, `inplace=True` can be added.
    print(df_cleaned.info())

    print_separator("Fill Missing Values")
    filled_df = df.fillna(130)
    print(filled_df.info())


if __name__ == "__main__":
    pandas_intro()
    clean_and_inspect_csv("data.csv")
