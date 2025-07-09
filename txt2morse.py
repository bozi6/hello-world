#  txt2morse.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 07. 09. 13:29
from datetime import datetime

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'
}


def text2morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
            morse_code.append(',')
        else:
            morse_code.append('/')
    return ' '.join(morse_code)


def calculate_year(birth):
    current_year = datetime.now().year
    age = current_year - birth
    return age


def main():
    szoveg = input("Enter text to convert to morse: ")
    morse = text2morse(szoveg)
    print('Morse code: ', morse)
    birth_year = int(input("Enter your birth year: "))
    age = calculate_year(birth_year)
    print(f"Your age is {age} years.")


if __name__ == "__main__":
    main()
