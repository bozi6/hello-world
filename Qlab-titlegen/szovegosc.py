import client

cli = client.Interface()


def main():
    try:
        file = open('example-input.txt')
        """
        A szövegfájlban ha több sort akarunk akkor /-el kell a sorokat elválasztani
        Ha üres sort akakrunk akkor .-ot kell tenni a sorba
        """
        start_number = 1000  # A cue kezdőszáma
        last_blank = True
        last_titles_was_decimal = False
        for line in file.readlines():
            line = line[:-1]
            this_cue = start_number + 1
            this_blank = line == '.'
            broken_line = line.replace('/', '\n')
            if not last_blank:
                cli.newcue('fade')
                ctn = str(start_number) + '.1' if last_titles_was_decimal else str(start_number)
                sn = 'Üres' if this_blank else str(start_number) + ' FO&S'
                cucc = (
                    (b'/cue/selected/stopTargetWhenDone', [1]),
                    (b'/cue/selected/duration', [0.3]),
                    (b'/cue/selected/doOpacity', [1]),
                    (b'/cue/selected/opacity', [0]),
                    (b'/cue/selected/number', [this_cue]),
                    (b'/cue/selected/cueTargetNumber', [bytes(ctn, 'utf-8')]),
                    (b'/cue/selected/name', [bytes(sn, 'utf-8')])
                )
                cli.bundi(cucc)
                if not this_blank:
                    cli.set_cue_prop('selected', 'continueMode', [2])
            if not this_blank:
                cli.newcue('text')
                tsn = str(this_cue) + '.1' if not last_blank else str(this_cue)
                cucc = (
                    (b'/cue/selected/number', [bytes(tsn, 'utf-8')]),
                    (b'/cue/selected/text/format/fontSize', [72]),
                    (b'/cue/selected/colorName', [b'green']),
                    (b'/cue/selected/translation/y', [-440]),
                    (b'/cue/selected/text/format/color', [1, 1, 0, 1]),
                    (b'/cue/selected/text', [bytes(broken_line, 'utf-8')]),
                    (b'/cue/selected/name', [bytes(line, 'utf-8')]),
                    (b'/cue/selected/fillStage', [0]),
                )
                cli.bundi(cucc)
            start_number = this_cue
            last_titles_was_decimal = not last_blank
            last_blank = this_blank
        #  cues = cli.getques()
        #  print(cues)
        cli.renumber(10, 1)
        """
        for id,number,uid,type in cues:
            print(id)
            print(number)
            print(uid)
            print(type)
        cli.select_all_cues()
        """
    except IOError:
        print("Nem lehet megnyitni a fájlt.")


if __name__ == '__main__':
    main()
