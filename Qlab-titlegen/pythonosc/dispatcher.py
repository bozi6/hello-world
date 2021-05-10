import pyOSC3

import qlabdef

ifa = qlabdef.Interface()


def main():
    try:
        file = open('./example-input.txt')
    except IOError:
        print('File not found')
    last_cue = 200
    last_blank = True
    last_titles_was_decimal = False
    for line in file.readlines():
        line = line[:-1]
        this_cue = last_cue + 1
        this_blank = line == '.'
        broken_line = line.replace('/', '\n')
        if not last_blank:
            ifa.newcue('fade')
            ifa.set_cue_prop('selected', 'stopTargetWhenDone', [1])
            ifa.set_cue_prop('selected', 'duration', [0.5])
            ifa.set_cue_prop('selected', 'doOpacity', 1)
            ifa.set_cue_prop('selected', 'opacity', 0)
            ifa.set_cue_prop('selected', 'number', [str(this_cue)])
            ifa.set_cue_prop('selected', 'cueTargetNumber', str(last_cue) + '.1' if last_titles_was_decimal else str(last_cue))
            ifa.set_cue_prop('selected', 'name', 'Üres' if this_blank else str(last_cue)+' FO')
            if not this_blank:
                ifa.set_cue_prop('selected', 'continueMode', [2])
        if not this_blank:
            ifa.newcue('text')
            ifa.set_cue_prop('selected', 'number', [str(this_cue) + '.1' if not last_blank else str(this_cue)])
            ifa.set_cue_prop('selected', 'text/format/fontSize', 72)
            ifa.set_cue_prop('selected', 'colorName', 'green')
            ifa.set_cue_prop('selected', 'translationY', -440)
            ifa.client.send(pyOSC3.OSCMessage('/cue/selected/text/format/color', [1, 1, 0, 1]))
            # ifa.set_cue_prop('selected', 'text/format/color' [1, 0, 0, 1])
            ifa.set_cue_prop('selected', 'text', broken_line)
            ifa.set_cue_prop('selected', 'name', line)
        last_cue = this_cue
        last_titles_was_decimal = not last_blank
        last_blank = this_blank


"""
c.send(OSCMessage("/cue/1/name", ['Balfassz']))
c.send(OSCMessage("/cue/1/text", 'Árvíztűrő tükörfúrógép'))
c.send(OSCMessage("/cue/1/text/format/color", [1, 0, 0, 0.5]))
/cue/{cue_no}/{name}
"""

if __name__ == '__main__':
    main()
