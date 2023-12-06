import time

str2 = time.time()


def findprime(startnumber, endnumber):
    """
    A prímszámokat keresi meg
    :param startnumber: a kezdő szám
    :param endnumber: a vége szám
    :return: a megtalált prímszámok listája
    """
    start = time.time()
    primes = []
    no_primes = 0

    for candidate_number in range(startnumber, endnumber, 1):
        found_prime = True
        for div_number in range(2, candidate_number):
            if candidate_number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(candidate_number)
            no_primes += 1

    end = round(time.time() - start, 4)

    print("Az összes prímszám megkeresése " + str(endnumber) + "-ig")
    print("Eltelt idő: " + str(end) + " másodperc")
    print("Megtalált prímszámok: " + str(no_primes))
    return primes


def insert_newlines(string, every=128):
    """
    Minden 128-ik karakterhez beszúr egy újsor karaktert
    :param string: a bejövő karakterlánc
    :param every: hova szúrja be az újsor karaktert
    :return: a feldarabolt string
    """
    return "\n".join(string[i : i + every] for i in range(0, len(string), every))


def main():
    """
    Main program
    :return: Print out find first 10000 prime number
    """
    pr = findprime(1, 10000)
    soros = insert_newlines(
        "Helló ez egy hosszú string akar lenni, amibe a python beletesz,"
        "elvileg minden 128-ik karakternél"
        " egy jó kis újsor karaktert, amivel aztán lehet"
        " hogy hosszabb lófaszok is bekerülhetnek, mert az"
        " nagyon jó nekünk."
    )

    print(soros)
    print("Ja a megtalált számok: \n" + insert_newlines(str(pr)))
    vege = round(time.time() - str2, 4)
    print("És a teljes futásidő: " + str(vege) + " sec.")


if __name__ == "__main__":
    main()
