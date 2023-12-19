def szamol(dmx: float):
    """
    dmx átszámolása valami teljesen mássá...

    :param dmx: Dmx address to calculate
    :type dmx: int
    :return: DMX százalékba átszámolva.
    :rtype: percent

    """
    dmx = dmx.replace(",", ".")
    if dmx is None:
        return 0
    try:
        dmx = float(dmx)
        if float(dmx) > 255:
            print("nem lehet nagyobb 255-nél.")
            return 0
        ered = (float(dmx) / 255) * 100
        return ered
    except ValueError:
        return 0
    return ered


if __name__ == "__main__":
    while True:
        cuc = input(" dmx:")
        a = szamol(cuc)
        print("{:.2f}%".format(a))
