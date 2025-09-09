import csv  # kell a CSV fájlokhoz

def process_csv(input_file, output_file):
    names = []  # nevek gyűjtésére
    ages = []   # életkorok gyűjtésére

    # megnyitjuk a bemeneti fájlt
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # fejléc átugrása

        for row in reader:
            # ellenőrizzük, hogy biztosan két oszlop van-e
            if len(row) != 2:
                print(f"Hibás sor kihagyva: {row}")
                continue

            name, age = row
            try:
                age = int(age)  # megpróbáljuk számmá alakítani
            except ValueError:
                print(f"Hibás életkor, kihagyva: {row}")
                continue

            names.append(name)
            ages.append(age)

    # ha nem sikerült egyetlen jó adatot sem beolvasni
    if not ages:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Nincs feldolgozható adat.\n")
        return

    # számítások
    average_age = sum(ages) / len(ages)
    oldest = names[ages.index(max(ages))]
    youngest = names[ages.index(min(ages))]

    # eredmények fájlba írása
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Átlagéletkor: {average_age:.2f}\n")
        f.write(f"Legidősebb: {oldest} ({max(ages)} év)\n")
        f.write(f"Legfiatalabb: {youngest} ({min(ages)} év)\n")

# példa futtatás
process_csv('people.csv', 'summary.txt')
