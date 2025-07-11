import sys
import string

# Define default character sets as a constant
HUNGARIAN_ALPHABET = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
DEFAULT_ALPHABETS = (HUNGARIAN_ALPHABET, HUNGARIAN_ALPHABET.upper(), string.digits)


def shift(alphabet, step):
    """
    Shift an alphabet by the specified number of positions.
    
    :param alphabet: Character set to shift
    :param step: Number of positions to shift
    :return: Shifted character set
    """
    step %= len(alphabet)
    return alphabet[step:] + alphabet[:step]


def caesar_cipher(text, step, alphabets=DEFAULT_ALPHABETS):
    """
    Encrypts text using a Caesar cipher with the specified shift step.
    
    :param text: Input text to encrypt
    :param step: Shift step, maximum is the size of the alphabet
    :param alphabets: Tuples of character sets to use for encryption
    :return: Encrypted text
    """
    shifted_alphabets = tuple(shift(alphabet, step) for alphabet in alphabets)
    combined_alphabets = "".join(alphabets)
    translated_alphabets = "".join(shifted_alphabets)
    translation_table = str.maketrans(combined_alphabets, translated_alphabets)
    return text.translate(translation_table)


def read_input_file(filename):
    """
    Read text content from a file.
    
    :param filename: Name of the file to read
    :return: Content of the file as a string
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

   
def main():
    input_filename = sys.argv[1] if len(sys.argv) > 1 else "test.txt"
    shift_step = 2
    text = read_input_file(input_filename)
    encrypted_text = caesar_cipher(text, step=shift_step)
    print(
        "Kiinduló szöveg: {}\nEltolt szöveg: {}\nEltolva {} lépéssel.".format(
            text, encrypted_text, shift_step
        )
    )


if __name__ == '__main__':
    main()
