KAPREKAR_KONSTANS = 6174
FOUR_DIGIT_FMT = "{:04d}"


def validate_four_digit_input(n: int) -> bool:
    """Ellenőrzi, hogy a szám 0..9999 között van-e és van-e legalább két különböző számjegy."""
    if not (0 <= n <= 9999):
        print("Hiba: 0 és 9999 közötti számot adj meg.")
        return False
    s = FOUR_DIGIT_FMT.format(n)
    if len(set(s)) == 1:
        print("Hiba: legalább két különböző számjegy szükséges (nem lehet minden számjegy azonos).")
        return False
    return True


def kaprekar_step(s: str) -> tuple[str, str, int]:
    """Egy Kaprekar-lépés: visszaadja (asc, desc, különbség)."""
    s_norm = FOUR_DIGIT_FMT.format(int(s))
    asc = "".join(sorted(s_norm, reverse=True))  # csökkenő (nagyobb)
    desc = "".join(sorted(s_norm))  # növekvő (kisebb)
    diff = int(asc) - int(desc)
    return asc, desc, diff


def kaprekar_6174_lepesek(n: int) -> int:
    """
    Kiírja a Kaprekar-eljárás lépéseit négyjegyű számra (legalább két különböző számjeggyel).
    Visszatér: a lépések száma (ha valid a bemenet, különben 0).
    Példa sor: 8742 - 2478 = 6264
    """
    # Bemenet ellenőrzése
    if not validate_four_digit_input(n):
        return 0

    s = FOUR_DIGIT_FMT.format(n)
    lepesek_szama = 0
    latott_kulonbsegek: set[int] = set()

    while True:
        lepesek_szama += 1
        asc, desc, kulonbseg = kaprekar_step(s)
        print(f"{asc} - {desc} = {FOUR_DIGIT_FMT.format(kulonbseg)}")

        if kulonbseg == KAPREKAR_KONSTANS:
            print(f"Elértük a {KAPREKAR_KONSTANS}-et {lepesek_szama}. lépésben.")
            return lepesek_szama

        # Ciklusvédelem (elvileg 6174-hez kell konvergálnia érvényes bemenetnél)
        if kulonbseg in latott_kulonbsegek:
            print("Ciklust észleltem, nem jut el 6174-ig ezzel a bemenettel.")
            return lepesek_szama
        latott_kulonbsegek.add(kulonbseg)

        s = FOUR_DIGIT_FMT.format(kulonbseg)


if __name__ == "__main__":
    try:
        be = input("Adj meg egy négyjegyű számot (legalább két különböző számjeggyel): ").strip()
        kaprekar_6174_lepesek(int(be))
    except ValueError:
        print("Hiba: egész számot adj meg.")
