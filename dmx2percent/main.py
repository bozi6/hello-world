def szamol(dmx):
    """
    dmx átszámolása valami teljesen mássá...
    """
    try:
        if dmx > 255:
            print('Nem lehet nagyobb 255 nél.')
            return 0
        ered = (dmx / 255) * 100
        return ered
    except ValueError:
        return 0


while True:
    cuc = input(' dmx:')
    a = szamol(int(cuc))
    print('{:.2f}'.format(a))
