# szovegoscai.py

import qlab_client

cli = qlab_client.Interface()

# Constants
FONT_SIZE = 72
TRANSLATION_Y = -440
TEXT_COLOR = [1, 1, 0, 1]
CUE_COLOR = b"green"


# Helper function to create "fade" cues
def create_fade_cue(cli, start_number, current_is_blank, last_title_was_decimal, next_cue_number):
    cue_number = f"{start_number}.1" if last_title_was_decimal else f"{start_number}"
    cue_name = "Üres" if current_is_blank else f"{start_number} FO&S"
    property_bundle = [
        (b"/cue/selected/stopTargetWhenDone", [1]),
        (b"/cue/selected/duration", [0.3]),
        (b"/cue/selected/doOpacity", [1]),
        (b"/cue/selected/opacity", [0]),
        (b"/cue/selected/number", [next_cue_number]),
        (b"/cue/selected/cueTargetNumber", [bytes(cue_number, "utf-8")]),
        (b"/cue/selected/name", [bytes(cue_name, "utf-8")]),
    ]
    cli.newcue("fade")
    cli.bundi(property_bundle)
    if not current_is_blank:
        cli.set_cue_prop("selected", "continueMode", [2])


# Helper function to create "text" cues
def create_text_cue(cli, line, broken_line, is_following_blank, next_cue_number):
    text_cue_number = f"{next_cue_number}.1" if not is_following_blank else str(next_cue_number)
    text_bundle = [
        (b"/cue/selected/number", [bytes(text_cue_number, "utf-8")]),
        (b"/cue/selected/text/format/fontSize", [FONT_SIZE]),
        (b"/cue/selected/colorName", [CUE_COLOR]),
        (b"/cue/selected/translation/y", [TRANSLATION_Y]),
        (b"/cue/selected/text/format/color", TEXT_COLOR),
        (b"/cue/selected/text", [bytes(broken_line, "utf-8")]),
        (b"/cue/selected/name", [bytes(line, "utf-8")]),
        (b"/cue/selected/fillStage", [0]),
    ]
    cli.newcue("text")
    cli.bundi(text_bundle)


def process_file(file_path):
    try:
        with open(file_path) as file:
            start_number = 1000
            previous_is_blank = True
            last_title_was_decimal = False

            for line in file:
                line = line.rstrip("\n")
                current_is_blank = (line == ".")
                broken_line = line.replace("/", "\n")
                next_cue_number = start_number + 1

                if not previous_is_blank:
                    create_fade_cue(cli, start_number, current_is_blank, last_title_was_decimal, next_cue_number)

                if not current_is_blank:
                    create_text_cue(cli, line, broken_line, previous_is_blank, next_cue_number)

                # Update variables for next iteration
                start_number = next_cue_number
                last_title_was_decimal = not previous_is_blank
                previous_is_blank = current_is_blank

            cues = cli.getques()
            if cues is not None:
                print("cues")
                print(cues)
                cli.renumber(10, 1)
    except IOError:
        print("Nem lehet megnyitni a fájlt.")


if __name__ == "__main__":
    process_file("example-input.txt")
