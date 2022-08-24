import math

GRAV = 9.81
fiszog = 0  # Az elhajított tárgy hajítási irányának vízszintessel bezárt szöge
vkezd = 0  # A tárgy kezdősebesége
magassag = 0  # A pálya kezdőmagassága a földhöz kéőpest
dist = 0  # tárgy vízszintes útja
time = 0  # repülési idő


def visztav(vkezd, fiszog, magassag=0):
    a = (vkezd * math.cos(math.radians(fiszog))) / GRAV
    b = vkezd * math.sin(math.radians(fiszog))
    c = b ** 2
    d = 2*(GRAV*magassag)
    if magassag == 0:
        tavolsag = (vkezd**2*math.sin(2*math.radians(fiszog)))/GRAV
    else:
        tavolsag = a * (b + math.sqrt(c + d))
    return tavolsag


def repido(tavolsag, vk, fisz):
    ido = tavolsag / (vk * math.cos(fisz))
    return ido


tav = visztav(10, 45, 2.5)
print(tav, "méter")
print(repido(tav, 10, 45), " sec")
