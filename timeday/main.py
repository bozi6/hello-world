#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
import sys
import calendar
from datetime import datetime, date

DATA_FILE = "worklog.csv"
DATE_FMT = "%Y-%m-%d"
TIME_FMT = "%H:%M"

HEADERS = ["name", "date", "start", "end", "PN"]

# ------------------------------ Segédfüggvények ------------------------------

def ensure_csv_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(HEADERS)

def load_rows():
    ensure_csv_exists()
    rows = []
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows

def save_rows(rows):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS)
        w.writeheader()
        for row in rows:
            w.writerow(row)

def list_users(rows):
    return sorted(set(r["name"] for r in rows if r.get("name")))

def parse_time_hhmm(s):
    try:
        dt = datetime.strptime(s, TIME_FMT)
        return dt.hour, dt.minute
    except ValueError:
        return None

def time_diff_minutes(start_str, end_str):
    """Visszaadja a percek számát két HH:MM között. Csak ugyanazon a napon értelmezett."""
    ps = parse_time_hhmm(start_str)
    pe = parse_time_hhmm(end_str)
    if not ps or not pe:
        return None
    sh, sm = ps
    eh, em = pe
    start_min = sh * 60 + sm
    end_min = eh * 60 + em
    if end_min < start_min:
        return None  # nem támogatjuk az átlógást
    return end_min - start_min

def input_hhmm(prompt):
    s = input(prompt).strip()
    if s == "":
        return None
    if parse_time_hhmm(s):
        return s
    print("Hibás időformátum. Használd: ÓÓ:PP, pl. 07:30")
    return None

def input_date_yyyy_mm_dd(prompt, default=None):
    s = input(prompt).strip()
    if not s and default:
        return default
    try:
        # Elfogad 2025-09-03 formátumot
        datetime.strptime(s, DATE_FMT)
        return s
    except ValueError:
        print("Hibás dátum. Használd: ÉÉÉÉ-HH-NN, pl. 2025-09-03")
        return None

def input_year_month(prompt, default_year, default_month):
    s = input(prompt).strip()
    if not s:
        return default_year, default_month
    try:
        y, m = s.split("-")
        y, m = int(y), int(m)
        if 1 <= m <= 12:
            return y, m
    except Exception:
        pass
    print("Hibás formátum. Használd: ÉÉÉÉ-HH, pl. 2025-09")
    return None, None

def find_row(rows, name, day):
    for r in rows:
        if r["name"] == name and r["date"] == day:
            return r
    return None

def upsert_row(rows, name, day, start=None, end=None, pn=None):
    r = find_row(rows, name, day)
    if r is None:
        r = {"name": name, "date": day, "start": "", "end": "", "PN": ""}
        rows.append(r)
    if start is not None:
        r["start"] = start
    if end is not None:
        r["end"] = end
    if pn is not None:
        r["PN"] = pn

def fmt_hhmm_from_minutes(total_minutes):
    h = total_minutes // 60
    m = total_minutes % 60
    return f"{h:02d}:{m:02d}"

# ------------------------------ Fő funkciók ------------------------------

def choose_or_create_user(rows):
    users = list_users(rows)
    if users:
        print("\nLétező felhasználók:")
        for i, u in enumerate(users, 1):
            print(f"  {i}. {u}")
    else:
        print("\nMég nincs felhasználó.")

    name = input("Név (új vagy meglévő): ").strip()
    if not name:
        print("Név nem lehet üres.")
        return None
    # Ha nem létezett, csak simán létrejön első mentéskor
    return name

def set_today_start(rows, name):
    today = date.today().strftime(DATE_FMT)
    while True:
        t = input_hhmm("Mai kezdés (ÓÓ:PP): ")
        if t is None:
            continue
        upsert_row(rows, name, today, start=t, pn="")
        save_rows(rows)
        print(f"Kezdés rögzítve: {today} {t}")
        return

def set_today_end(rows, name):
    today = date.today().strftime(DATE_FMT)
    r = find_row(rows, name, today)
    if r is None or not r.get("start"):
        print("Előbb add meg a mai kezdést.")
        return
    while True:
        t = input_hhmm("Mai befejezés (ÓÓ:PP): ")
        if t is None:
            continue
        # Validáld időrendet
        if time_diff_minutes(r["start"], t) is None:
            print("A befejezés nem lehet korábban, mint a kezdés.")
            continue
        upsert_row(rows, name, today, end=t, pn="")
        save_rows(rows)
        print(f"Befejezés rögzítve: {today} {t}")
        return

def set_given_day_start(rows, name):
    while True:
        d = input_date_yyyy_mm_dd("Dátum (ÉÉÉÉ-HH-NN): ")
        if not d:
            continue
        t = input_hhmm("Kezdés (ÓÓ:PP): ")
        if t is None:
            continue
        upsert_row(rows, name, d, start=t, pn="")
        save_rows(rows)
        print(f"Kezdés rögzítve: {d} {t}")
        return

def set_given_day_end(rows, name):
    while True:
        d = input_date_yyyy_mm_dd("Dátum (ÉÉÉÉ-HH-NN): ")
        if not d:
            continue
        r = find_row(rows, name, d)
        if r is None or not r.get("start"):
            print("Előbb add meg az adott nap kezdését.")
            continue
        t = input_hhmm("Befejezés (ÓÓ:PP): ")
        if t is None:
            continue
        if time_diff_minutes(r["start"], t) is None:
            print("A befejezés nem lehet korábban, mint a kezdés.")
            continue
        upsert_row(rows, name, d, end=t, pn="")
        save_rows(rows)
        print(f"Befejezés rögzítve: {d} {t}")
        return

def month_stats(rows, name):
    today = date.today()
    y, m = input_year_month(
        f"Statisztika hónapra (ÉÉÉÉ-HH, Enter = {today.year}-{today.month:02d}): ",
        today.year, today.month
    )
    if not y:
        return

    _, days_in_month = calendar.monthrange(y, m)
    month_days = [date(y, m, d).strftime(DATE_FMT) for d in range(1, days_in_month + 1)]

    # Összegzés és PN/N/A kitöltés
    total_minutes = 0
    rest_days = 0
    changed = False

    for d in month_days:
        r = find_row(rows, name, d)
        if r and r.get("start") and r.get("end"):
            diff = time_diff_minutes(r["start"], r["end"])
            if diff is None:
                # Rossz adat: nem számoljuk, de nem piszkáljuk.
                if r and r.get("PN") == "PN":  # Explicit PN check
                    rest_days += 1
                else:
                    pas5s
            else:
                total_minutes += diff
        else:
            # Hiányzó nap → jelöld PN + N/A
            # Ha nincs sor, hozzuk létre
            if r is None or (not r.get("start") and not r.get("end") and r.get("PN") != "PN"):
                upsert_row(rows, name, d, start="N/A", end="N/A", pn="PN")
                changed = True

            elif not r or (not r.get("start") and not r.get("end")):  # Missing or empty day
                rest_days += 1

    if changed:
        save_rows(rows)

    print("\n--- Statisztika ---")
    print(f"Név: {name}")
    print(f"Hónap: {y}-{m:02d}")
    print(f"Ledolgozott idő: {fmt_hhmm_from_minutes(total_minutes)}")
    print(f"Pihenőnapok (PN): {rest_days}")
    print("(Hiányzó napok PN-ként és N/A időkkel rögzítve a CSV-ben.)")

# ------------------------------ Fő ciklus ------------------------------

def main():
    rows = load_rows()
    current_user = None

    while True:
        print("\nMunkaidő nyilvántartó")
        print("---------------------")
        print("1. Mai kezdés")
        print("2. Mai befejezés")
        print("3. Adott nap kezdés")
        print("4. Adott nap végzés")
        print("5. Statisztika")
        print("6. Név (választás/létrehozás)")
        print("0. Kilépés")
        if current_user:
            print(f"(Aktív név: {current_user})")
        choice = input("Választás: ").strip()

        if choice == "0":
            print("Viszlát.")
            return

        if choice == "6":
            name = choose_or_create_user(rows)
            if name:
                current_user = name
            continue

        if not current_user:
            print("Előbb válassz nevet a 6. menüponttal.")
            continue

        if choice == "1":
            set_today_start(rows, current_user)
        elif choice == "2":
            set_today_end(rows, current_user)
        elif choice == "3":
            set_given_day_start(rows, current_user)
        elif choice == "4":
            set_given_day_end(rows, current_user)
        elif choice == "5":
            month_stats(rows, current_user)
        else:
            print("Ismeretlen választás.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMegszakítva.")
        sys.exit(1)