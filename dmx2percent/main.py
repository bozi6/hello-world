ERR_MSG_MAXIMUM_EXCEEDED = "A DMX érték nem lehet nagyobb 255-nél."


def convert_to_float(value: str) -> float:
    """
    Stringet float típusra konvertál, vesszők ponttá alakításával.

    :param value: A bemeneti karakterlánc.
    :return: A konvertált float érték, vagy 0, ha nem érvényes.
    """
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return 0


def dmx_to_percent(dmx: str) -> float:
    """
    DMX értéket százalékba konvertál.

    :param dmx: DMX cím string formátumban.
    :return: Százalékos érték a 0-100 tartományban.
    """
    if not dmx:
        return 0

    dmx_value = convert_to_float(dmx)

    if dmx_value > 255:
        print(ERR_MSG_MAXIMUM_EXCEEDED)
        return 0

    percent_value = (dmx_value / 255) * 100
    return percent_value


if __name__ == "__main__":
    print("Program fut... Nyomd meg az 'q'-t a kilépéshez!")
    while True:
        user_input = input("DMX érték: ")
        if user_input.strip().lower() == "q":
            print("Kilépés...")
            break
        calculated_percent = dmx_to_percent(user_input)
        print("{:.2f}%".format(calculated_percent))
