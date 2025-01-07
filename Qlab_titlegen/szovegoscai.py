#  szovegoscai.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 01. 07. 9:34

import qlab_client

cli = qlab_client.Interface()


def process_file(file_path):
    try:
        with open(file_path) as file:
            start_number = 1000
            last_blank = True
            last_titles_was_decimal = False

            for line in file:
                line = line.rstrip("\n")
                this_cue = start_number + 1
                this_blank = (line == ".")
                broken_line = line.replace("/", "\n")

                if not last_blank:
                    cli.newcue("fade")
                    cue_number = (f"{start_number}.1" if last_titles_was_decimal else f"{start_number}")
                    cue_name = "Üres" if this_blank else f"{start_number} FO&S"

                    property_bundle = [
                        (b"/cue/selected/stopTargetWhenDone", [1]),
                        (b"/cue/selected/duration", [0.3]),
                        (b"/cue/selected/doOpacity", [1]),
                        (b"/cue/selected/opacity", [0]),
                        (b"/cue/selected/number", [this_cue]),
                        (b"/cue/selected/cueTargetNumber", [bytes(cue_number, "utf-8")]),
                        (b"/cue/selected/name", [bytes(cue_name, "utf-8")]),
                    ]
                    cli.bundi(property_bundle)

                    if not this_blank:
                        cli.set_cue_prop("selected", "continueMode", [2])

                if not this_blank:
                    cli.newcue("text")
                    text_cue_number = (f"{this_cue}.1" if not last_blank else str(this_cue))
                    text_bundle = [
                        (b"/cue/selected/number", [bytes(text_cue_number, "utf-8")]),
                        (b"/cue/selected/text/format/fontSize", [72]),
                        (b"/cue/selected/colorName", [b"green"]),
                        (b"/cue/selected/translation/y", [-440]),
                        (b"/cue/selected/text/format/color", [1, 1, 0, 1]),
                        (b"/cue/selected/text", [bytes(broken_line, "utf-8")]),
                        (b"/cue/selected/name", [bytes(line, "utf-8")]),
                        (b"/cue/selected/fillStage", [0]),
                    ]
                    cli.bundi(text_bundle)

                start_number = this_cue
                last_titles_was_decimal = not last_blank
                last_blank = this_blank

            cues = cli.getques()
            if cues is not None:
                print("cues")
                print(cues)
                cli.renumber(10, 1)

    except IOError:
        print("Nem lehet megnyitni a fájlt.")


if __name__ == "__main__":
    process_file("example-input.txt")
