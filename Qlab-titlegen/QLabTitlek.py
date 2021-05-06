import qlabdef

ifa = qlabdef.Interface()
cli = qlabdef.Client()


def main():
    # file = open(args.file)
    try:
        file = open("./hutlen_dalszovegek_sima.txt")
    except IOError:
        print("File not found.")
    last_cue = 300  # newly created cue start number
    last_blank = True
    last_titles_was_decimal = False
    """    ifa.newcue('group')  # Create new group cue
    csoportid = ifa.get_cue_id() # Get uniquiId from group cue
    ifa.set_cue_property('selected', 'number', str(last_cue))  # Set group cue number to last_cue
    ifa.set_cue_property('selected', 'name', csoportid[:8])
    ifa.set_cue_property('selected', 'mode', 2)  # Change group mode to 2 (It is 3 in mode box in QLab)
    ifa.newcue('text')  # Create new Text cue
    szovegid = ifa.get_cue_id() # Get Text cue uniqueID
    ifa.set_cue_property('selected', 'text', szovegid[:8]) # Set text cue name to first 8 char of uniqueID
    ifa.movecue(szovegid, csoportid, 1)  # Try to move text cue under group cue
    ifa.renumber_cues(900, 1)
    print("gid: {}, text cue: {}".format(csoportid, szovegid))  # Print group and text cue uniqueID-s
    """

    for line in file.readlines():
        line = line[:-1]
        this_cue = last_cue + 1
        this_blank = line == '.'
        broken_line = line.replace('/', '\n')
        ifa.newcue('group')
        csopid = ifa.get_cue_id()
        if not last_blank:
            ifa.newcue('fade')
            fadid = ifa.get_cue_id()
            ifa.set_cue_property('selected', 'stopTargetWhenDone', 1)
            ifa.set_cue_property('selected', 'duration', 0.5)
            ifa.set_cue_property('selected', 'doOpacity', 1)
            ifa.set_cue_property('selected', 'opacity', 0)
            ifa.set_cue_property('selected', 'number', str(this_cue))
            ifa.set_cue_property('selected', 'cueTargetNumber', str(last_cue) + '.1' if last_titles_was_decimal else str(last_cue))
            ifa.set_cue_property('selected', 'name', 'Üres' if this_blank else str(last_cue)+' FO')
            if not this_blank:
                ifa.set_cue_property('selected', 'continueMode', 2)
            ifa.movecue(fadid, csopid, 2)
        if not this_blank:
            ifa.newcue('text')
            txtid = ifa.get_cue_id()
            ifa.set_cue_property('selected', 'number', str(this_cue) + '.1' if not last_blank else str(this_cue))
            ifa.set_cue_property('selected', 'text/format/fontSize', 72)
            ifa.set_cue_property('selected', 'colorName', 'green')
            ifa.set_cue_property('selected', 'text', broken_line)
            ifa.set_cue_property('selected', 'name', line)
            ifa.movecue(txtid, csopid, 1)
        print("csid: {} - cueid: {}".format(csopid, txtid,))
        last_cue = this_cue
        last_titles_was_decimal = not last_blank
        last_blank = this_blank




if __name__ == '__main__':
    main()
