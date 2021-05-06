import qlabdef

interface = qlabdef.Interface()


def main():
    # file = open(args.file)
    try:
        file = open("./example-input.txt")
    except IOError:
        print("File not found.")
    last_cue = 300  # newly created cue start number
    last_blank = True
    last_titles_was_decimal = False

    interface.newcue('group')  # Create new group cue
    csoportid = interface.get_cue_id()  # Get uniquiId from group cue
    interface.set_cue_property('selected', 'number', str(last_cue))  # Set group cue number to last_cue
    interface.set_cue_property('selected', 'name', csoportid[:8])  # Set group cue name to 8 character from uniqueID
    interface.set_cue_property('selected', 'mode', 2)  # Change group mode to 2 (It is 3 in mode box in QLab)
    interface.newcue('text')  # Create new Text cue
    szovegid = interface.get_cue_id()  # Get Text cue uniqueID
    interface.set_cue_property('selected', 'text', szovegid[:8])  # Set text cue name to first 8 char of uniqueID
    interface.movecue(szovegid, csoportid, 1)  # Try to move text cue under group cue
    interface.renumber_cues(900, 1)
    print("gid: {}, text cue: {}".format(csoportid, szovegid))  # Print group and text cue uniqueID-s


if __name__ == '__main__':
    main()