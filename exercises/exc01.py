def reverse_words(Sentence):
    words = Sentence.split(" ")
    new_word_list = [word[::-1] for word in words]
    res_str = " ".join(new_word_list)
    return res_str


# Given string
str1 = "My Name is Jessa"
print(reverse_words(str1))
