#  coolnum.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 01. 21. 22:08

# The number 6174
#
# Also known as Kaprekar’s constant,
# this number has a special feature
# if you follow the below steps
# (Taken from various sources, but let’s just say Wikipedia):
#
# Take any four-digit number (at least two digits should be different).
# Arrange the digits in descending and
# ascending order to get two new four-digit numbers.
# Now, subtract the smaller number from the bigger number.
# Redo step 2.
# If you do this for multiple steps,
# you will always end up with 6174 and
# that is the mysterious thing about.
# Why do we always end up with this number
# no matter which numbers you start with.
#
# Let’s take an example of 2714:
#
# 7421 -1247 = 6174
# Another example of 3687:
#
# 8763 -3678 = 5085;
#
# 8550 -0558 = 7992;
#
# 9972 -2799 = 7173;
#
# 7731 -1377 = 6354;
#
# 6543 -3456 = 3087;
#
# 8730 -0378 = 8352;
#
# 8532 -2358 = 6174
#
# Now, if we have 6174, we will always stay at 6174 because 7641 -1467 = 6174.
#
# It is also a Harshad number,
# meaning it is divisible by the sum
# of its constituents:
# 6174 / (6 + 1 + 7 + 4) = 6174 / 18 = 343.
# So, that adds to its coolness.

def __main__(szam):
    szam = int(szam)

    def getSortedNumber(number):
        num = str(number)
        asc = ''.join(sorted(num, reverse=True))
        desc = ''.join(sorted(num))
        if asc > desc:
            vissz = int(asc)-int(desc)
        else:
            vissz = int(desc)-int(asc)
        if vissz != 6147:
            getSortedNumber(vissz)


        return vissz

    if type(szam) != int:
        print(f'a {szam} nem egész szám')
    elif szam < 1000:
        print('Négyjegyű számot kell megadni.')
    elif szam > 9999:
        print('Négyjegyű számot kell megadni.')
    else:
        print(getSortedNumber(szam))


if __name__ == '__main__':
    szam = input('Írjá négyjegyű számot:')
    __main__(szam)
