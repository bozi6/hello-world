import turtle

"""
Közlekedési lámpa rajzolása
"""
allapot_sorszam = 0


def main():
    """
    Főprogram lámpa rajzolása szépen
    :return: egy közlekedési lámpa
    :rtype: turtle object

    """
    turtle.setup(400, 500)
    ablak = turtle.Screen()
    ablak.title("Eszti közlekedési lámpává válik.")
    ablak.bgcolor("lightgreen")
    Eszti = turtle.Turtle()

    def doboz_rajzolas():
        """Egy csinos doboz rajzolása a közlekedési lámpa számára
        :rtype: turtle box
        """
        Eszti.pensize(3)
        Eszti.color("black", "darkgrey")
        Eszti.begin_fill()
        Eszti.forward(80)
        Eszti.left(90)
        Eszti.forward(200)
        Eszti.circle(40, 180)
        Eszti.forward(200)
        Eszti.left(90)
        Eszti.end_fill()

    doboz_rajzolas()

    Eszti.penup()
    # Eszti pozicionálása oda, ahol a zöld lámápnak kell lennie
    Eszti.forward(40)
    Eszti.left(90)
    Eszti.forward(50)
    # Esztit nagy zöld körré alakítjuk át
    Eszti.shape("circle")
    Eszti.shapesize(3)
    Eszti.fillcolor("green")

    """ A közlekedési lámpa egyfajta állapotautomata, három állapottal:
     zölddel, sárgával és pirossal. Az állapotokat rendre
     0, 1, 2 számokkal írjuk le.
     Az állapotváltozásnál Eszti helyzetét és színét változtatjuk meg.
     """

    def allapot_automata_esemenykezeloje():
        global allapot_sorszam
        if allapot_sorszam == 0:  # Átmeneet a 0. állapotból az 1. állapotba
            Eszti.forward(70)
            Eszti.fillcolor("orange")
            allapot_sorszam = 1
        elif allapot_sorszam == 1:  # Átmeneet a 1. állapotból az 2. állapotba
            Eszti.forward(70)
            Eszti.fillcolor("red")
            allapot_sorszam = 2
        else:  # Átmeneet a 2. állapotból az 0. állapotba
            Eszti.back(140)
            Eszti.fillcolor("green")
            allapot_sorszam = 0

    # Az eseménykezelőt a space billentyűhöz kötjük
    ablak.onkey(allapot_automata_esemenykezeloje, "space")
    ablak.listen()
    ablak.mainloop()


if __name__ == "__main__":
    main()
