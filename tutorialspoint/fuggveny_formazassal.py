def valami(*args, **kwargs):
    """
    visszaadja a belerúgott argumentumokat.
    :param args: akármennyi egy db argumentum lehet
    :param kwargs: nevesített argumentumok, így faszább
    :return: semmit nem ad vissza egyenlőre, mert csak kiírja azokat.
    """
    for a in args:
        print(f'argumentum: {a}')
    for k in kwargs:
        print(f'Kulcs: {k:>15}\nÉrték: {kwargs[k]:>15}\n{'.'*22}')
        """
        az f az hogy változókat akarok rakni a {} közé
        a {} között a : az hogy formázni akarom
        a > jobbra igazít 15 space-nyit
        az utolsó '.'*24 24 db pötyöt ír ki, majd a :
        miatt formázza 40 spaceval a ^(alt+á a macen) miatt.
        """


valami(1, 2, 3, beszolas='qrvaanyád', kedvesszo='suka', forditas='bjlaty')
