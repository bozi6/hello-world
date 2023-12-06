import string


def main():
    """
    Main program
    :return: prints encoded text
    """
    alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)

    def caesar(text, step, alphabets):
        """
        :param text: Bejövő szöveg
        :param step: Az eltolás lépése, max 25 lehet
        :param alphabets: milyen szöveg alapján
        :return: az eltolt szöveget adja vissza
        """

        def shift(alphabet):
            return alphabet[step:] + alphabet[:step]

        shifted_alphabets = tuple(map(shift, alphabets))
        joined_alphabets = "".join(alphabets)
        joined_shifted_alphabets = "".join(shifted_alphabets)
        table = str.maketrans(joined_alphabets, joined_shifted_alphabets)
        return text.translate(table)

    with open("test.txt", "r") as file:
        szoveg = file.read()
    lepesek = 2
    cezar = caesar(szoveg, step=lepesek, alphabets=alphabets)
    print(
        "Kiinduló szöveg: {}\nEltolt szöveg: {}\nEltolva {} lépéssel.".format(
            szoveg, cezar, lepesek
        )
    )
    file.close()
