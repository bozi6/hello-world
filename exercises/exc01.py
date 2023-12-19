def reverse_words(Sentence):
    """
    Reversing wodrs in a sentence

    :param Sentence: Bejövő mondat
    :type Sentence: str
    :return: Reversed sentence
    :rtype: str

    """
    words = Sentence.split(" ")
    new_word_list = [word[::-1] for word in words]
    res_str = " ".join(new_word_list)
    return res_str


if __name__ == "__main__":
    # Given string
    str1 = "My Name is Jessa"
    print(reverse_words(str1))
