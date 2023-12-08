if __name__ == "__main__":
    ascii_dict = {"A": 65, "B": 66, "C": 67, "D": 68}
    # Reverse mapping
    new_dict = {value: key for key, value in ascii_dict.items()}
    print(new_dict)
