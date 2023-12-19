dictionary = {"A": 65, "B": 66, "C": 67, "D": 68}


def revmap(asci_dict):
    """
    Reverse mapping a dictionary (the key's will be the values and values will be the keys.)

    :param asci_dict: dictionari with keys and values
    :type asci_dict: dict
    :return: Reverse mapped dictionary
    :rtype: dict

    """
    # Reverse mapping
    new_dict = {value: key for key, value in asci_dict.items()}
    print(new_dict)


if __name__ == "__main__":
    revmap(dictionary)
