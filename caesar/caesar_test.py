import string


def caesar_cipher(text, step, alphabets):
    """
    Caesar cipher encryption
    
    :param text: Input text to encrypt
    :param step: Shift step, max 25
    :param alphabets: Character sets to use for encryption
    :return: Encrypted text
    """

    def shift(alphabet):
        """
        Shift alphabet by step positions
        
        :param alphabet: Character set to shift
        :return: Shifted character set
        """
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_alphabets = "".join(alphabets)
    joined_shifted_alphabets = "".join(shifted_alphabets)
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets)
    return text.translate(table)


def read_input_file(filename):
    """
    Read text from input file
    
    :param filename: Name of the file to read
    :return: File content as string
    """
    with open(filename, "r") as file:
        return file.read()


def main():
    """
    Main program
    
    :return: prints encoded text
    :rtype: str
    """
    alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)

    text = read_input_file("test.txt")
    shift_steps = 2
    encrypted_text = caesar_cipher(text, step=shift_steps, alphabets=alphabets)

    print(
        "Kiinduló szöveg: {}\nEltolt szöveg: {}\nEltolva {} lépéssel.".format(
            text, encrypted_text, shift_steps
        )
    )
