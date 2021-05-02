import qlabdef

interface = qlabdef.Interface()


def main():
    # file = open(args.file)
    try:
        file = open("./example-input.txt")
    except IOError:
        print("Nem található a fájl.")
    # A lényeg, hogy előbb jönnek a fade cuek, amik eltüntetik az előző szöveget.
    # és csak aztán jelenik meg az újabb szöveg.
    last_cue = 300  # az újonnan kezdődő cue-k száma
    last_blank = True  # utolsó sor üres volt-e?
    last_titles_was_decimal = False
    """
    Ide akarom a groupokat beszúrni, de nem akarja az új que-t belecsinálni.
    a group mode oscnél az:
     1-es a 2-es mode igazából
     a 2-es a 3-as
     a 3-as az 1-es
     es a 4-es a 4-es
     csak hogy egyértelmű legyen :-).

    """

    csoportid = interface.newcue('group')
    interface.set_cue_property('selected', 'number', str(last_cue))
    interface.set_cue_property('selected', 'name', 'szövegsor')
    interface.set_cue_property('selected', 'mode', 2)
    szovegid = interface.newcue('text')
    interface.set_cue_property('selected', 'text', 'szövegsor a fileból')
    interface.movecue(szovegid, csoportid, 1)
    print(csoportid, szovegid)

""" 
    send_msg(client, '/move/' + str(last_cue + 1), 1, 100)

    send_msg(client, '/disconnect')


if __name__ == '__main__':
    main()

    for line in file.readlines():  # sorok beolvasása
        line = line[:-1]
        this_cue = last_cue + 1  # Kezdőérték + 1
        this_blank = line == '.'
        broken_line = line.replace('/', '\n')
        if not last_blank:  # A fade cuek beállításai
            send_msg(client, '/new', 'fade')
            send_msg(client, '/cue/selected/stopTargetWhenDone', 1)
            send_msg(client, '/cue/selected/duration', 0.5)
            send_msg(client, '/cue/selected/doOpacity', 1)
            send_msg(client, '/cue/selected/opacity', 0)
            send_msg(client, '/cue/selected/number', str(this_cue))
            send_msg(client, '/cue/selected/cueTargetNumber',
                     str(last_cue) + '.1' if last_titles_was_decimal else str(last_cue))
            send_msg(client, '/cue/selected/name', 'ÜRES' if this_blank else str(last_cue)+' FO')
            if not this_blank:
                send_msg(client, '/cue/selected/continueMode', 2)
        if not this_blank:
            send_msg(client, '/new', 'text')
            send_msg(client, '/cue/selected/number', str(this_cue) + '.1' if not last_blank else str(this_cue))
            send_msg(client, '/cue/selected/text/format/fontSize', 64)
            send_msg(client, '/cue/selected/colorName', "green")
            send_msg(client, '/cue/selected/text', broken_line)
            # send_msg(client, '/cue/selected/name', line if last_blank else '--')
            send_msg(client, '/cue/selected/name', line)
        last_cue = this_cue
        last_titles_was_decimal = not last_blank
        last_blank = this_blank

    send_msg(client, '/disconnect')

"""
if __name__ == '__main__':
    main()

