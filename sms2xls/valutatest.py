import re

if __name__ == "__main__":
    tests = [
        (
            "...7878 Szàmla (120904) MUNKABÉR àTUTALàS:+142.934,-HUF; Közl:165; Partner:Honvéd Együttes Müvészeti; "
            "Egy:+763.192,-HUF; OTPdirekt",
            True,
        ),
        (
            "81009 16:19 Kàrtyàs vàsàrlàs/zàrolàs: -5.196 HUF; SPAR MAGYARORSZAG KFT, SPAR MAGYARORSZAG KFT; Kàrtyaszàm: "
            "...3535; Egyenleg: +2.355.736 HUF - OTPdirekt",
            True,
        ),
        (
            "...7878 Szàmla (130204) OTPdirekt HAVIDIJ:-254,-HUF; Egy:+653.844,-HUF; OTPdirekt",
            True,
        ),
        (
            "181022 13:09 Kàrtyàs vàsàrlàs/zàrolàs: -3.103,11 SEK; TICTAIL RUUTHIESSHOP, SE STOCKHOLM TICTAIL RU; "
            "Kàrtyaszàm: ...3535; Egy.: +2.137.174 HUF - OTPdirekt",
            True,
        ),
        (
            "130205 08:04 ATM készpénz felvét/zàrolàs: -50.000 HUF; OTP, BUDAPEST,HONVED KULT&amp;MEDI; Kàrtyaszàm: ...7782; "
            "Egyenleg: 714.343 HUF - OTPdirekt",
            True,
        ),
        (
            "181022 16:52 Kàrtyàs vàsàrlàs/zàrolàs: -8,48 CAD; A &amp; W # 4820, CA MALLORYTOWN A &amp; W # 4820; "
            "Kàrtyaszàm: ...3535; Egyenleg: +2.135.346 HUF - OTPdirekt",
            True,
        ),
        (
            "...7878 Szàmla (181026) VàSàRLàS KàRTYàVAL:-20.148,-HUF; Közl VàSàRLàS KàRTYàVAL          8925395276 "
            "0000000369583344; 61,630EUR; Egy:+2.079.239,-HUF; OTPdirekt",
            True,
        ),
        (
            "181028 01:14 Kàrtyàs vàsàrlàs/zàrolàs: -106,95 GBP; PAYPAL *LVB1G10, LU 35314369001 PAYPAL *LVB1G10; "
            "Kàrtyaszàm: ...5276; Egyenleg: +2.008.620 HUF - OTPdirekt",
            True,
        ),
        (
            "191123 13:29 Kàrtyàs vàsàrlàs: -1.075,50 SEK; PSN*freshmilk.se, SE Hovas PSN*freshmilk.se; Kàrtyaszàm: ...3535; "
            "Egyenleg: +2.033.538 HUF - OTPdirekt",
            True,
        ),
        (
            "220204 20:04 Kàrtyàs vàsàrlàs: -6.411 HUF; LIDL ARUHAZ 0235.SZ.; Kàrtyaszàm: ...7997; Egyenleg: +1.322.276 HUF "
            "- OTPdirekt",
            True,
        ),
        (
            "161215 16:19 Kàrtyàs vàsàrlàs/zàrolàs: -916 HUF; SPAR MAGYARORSZAG KFT; Kàrtyaszàm: 3535; Egyenleg: +1.867.814 "
            "HUF - OTPdirekt",
            False,
        ),
        (
            "Simple by OTP - Érintéses fizetés aktivàlàsàhoz szükséges 5 jegyü kòdod: HK4ME",
            True,
        ),
    ]

    regex = re.compile(r"(-|\+|\ )\d{1,}(\.|,|\s)(\d{1,3}|,)*.(\d{1,3}|\w{1,3});")
    for test, expected in tests:
        result = regex.match(test)
        is_match = result is not None
        print(test + "\t" + ("OK" if is_match == expected else "Fail"))
