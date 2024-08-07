def main():
    """
    String formázások pythonban

    :return: a formázott szövegek
    :rtype: str

    """
    # String formázók a Pythonban
    # String formázás az f-strings használatával
    print("<-------------Példa 1-------------------->")
    print("Írd be a neved")
    name = input()
    print(f"Hey !! {name}, üdvözlünk a buliban...")
    print("\n")
    print("<-------------Példa 2-------------------->")
    print("Írd be az első számot")
    a = int(input())
    print("Írd be a második számot")
    b = int(input())
    print(f"az {a} és {b} összege {a + b}")
    print("\n")
    # String formázás a format() eljárással
    print("<--------Alapvető sorrend------------>")
    str1 = "{} {} {}".format("Utazás", "az", "élet")
    print("A string az alapvető sorrendben van kiírva:")
    print(str1)
    print("<--------Pozíció szerinti formázás------------>")
    str2 = "{1} {2} {0}".format("szerelem", "Utazás", "egy")
    print(str2)
    print("<--------Kulcsszó szerinti formázás------------>")
    str3 = "{T} {i} {l}".format(T="Utazás", l="szerelem", i="egy")
    print(str3)
    print("\n")
    # String formázás a % operátor használatával
    print("Írd be az elemek számát")
    item = int(input())
    print("%s cipel %d tárgyat" % (name, item))

    # String methods Part 1
    string = "Különböző string metódusok"
    string2 = "  fektess a tanulásba       "
    print("lower()")
    print(string.lower())
    print("upper()")
    print(string.upper())
    print("islower()")
    print(string.islower())
    print("isupper()")
    print(string.isupper())
    print("startswith")
    print(string.startswith("Var"))
    print("endswith()")
    print(string.endswith("el"))
    print("join()")
    print("-->".join(["various", "strings", "methods"]))
    print("split()")
    print(string.split())
    print("ljust()")
    print("hello".ljust(15, "*"))
    print("rjust(*)")
    print("hello".rjust(15, "*"))
    print("center()")
    print("welcome".center(20, "*"))
    print("strip()>")
    print(string2.strip())
    print("lstrip()")
    print(string2.lstrip())
    print("rstrip()")
    print(string2.rstrip())

    # String methods --> Part 2
    string = "objektum orientált programozás"
    print("A string változó tartalma: ", string)
    print("index()")
    print("Az 'r' indexe az: '", string, "' szövegben:", string.index("r"))
    print("count()")
    print("Az 'o' számossága az '", string, "' szövegben:", string.count("o"))
    print("find()")
    print("A 'z' indexe az '", string, "' szövegben:", string.find("z"))
    print("replace()")
    print("icseréljük az 'e'-t '3'-ra :", string.replace("e", "3"))


if __name__ == "__main__":
    main()
