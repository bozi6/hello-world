import qlabdef

ifa = qlabdef.Interface()
cli = qlabdef.Client()


def main():
    # file = open(args.file)
    try:
        file = open("./example-input.txt")
    except IOError:
        print("File not found.")
    last_cue = 200  # newly created cue start number
    last_blank = True
    last_titles_was_decimal = False
    surf2 = ifa.get_surfaces()
    for line in file.readlines():
        line = line[:-1]
        this_cue = last_cue + 1
        this_blank = line == '.'
        broken_line = line.replace('/', '\n')
        if not last_blank:
            ifa.newcue('fade')
            ifa.set_cue_property('selected', 'stopTargetWhenDone', 1)
            ifa.set_cue_property('selected', 'duration', 0.5)
            ifa.set_cue_property('selected', 'doOpacity', 1)
            ifa.set_cue_property('selected', 'opacity', 0.001)
            ifa.set_cue_property('selected', 'number', str(this_cue))
            ifa.set_cue_property('selected', 'cueTargetNumber', str(last_cue) + '.1' if last_titles_was_decimal else str(last_cue))
            ifa.set_cue_property('selected', 'name', 'Üres' if this_blank else str(last_cue)+' FO')
            if not this_blank:
                ifa.set_cue_property('selected', 'continueMode', 2)
        if not this_blank:
            ifa.newcue('text')
            ifa.set_cue_property('selected', 'number', str(this_cue) + '.1' if not last_blank else str(this_cue))
            ifa.set_cue_property('selected', 'text/format/fontSize', 72)
            ifa.set_cue_property('selected', 'colorName', 'green')
            ifa.set_cue_property('selected', 'translationY', -440)
            ifa.set_cue_property('selected', 'text/format/color', [1, 1, 0, 1])
            ##  ifa.set_cue_property('selected', 'surfaceID', surf2[1]['surfaceID'])  # Mindig valtozik! és nem tudom átküldeni
            ifa.set_cue_property('selected', 'text', broken_line)
            ifa.set_cue_property('selected', 'name', line)
        last_cue = this_cue
        last_titles_was_decimal = not last_blank
        last_blank = this_blank


if __name__ == '__main__':
    main()
