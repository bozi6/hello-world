import pygdtf
import os
from termcolor import colored, cprint


def szinesben(mi, rizsa):
    print(mi, end='')
    cprint(rizsa, 'green')


def gdtfinfo(egy):
    # egy = pygdtf.FixtureType('./par64.gdtf')
    szinesben('Név: ', egy.name)
    szinesben('Rövid név: ', egy.short_name)
    szinesben('Hosszú név: ', egy.long_name)
    szinesben('Tárcsák:', egy.wheels)
    szinesben('Szűrők: ', egy.filters)
    szinesben('Színtér: ', egy.color_space.mode)
    szinesben('Leírás: ', egy.description)
    szinesben('DMX Profil: ', egy.dmx_profiles)
    szinesben('Lámpatípus Id: ', egy.fixture_type_id)
    szinesben('Gyártó: ', egy.manufacturer)
    try:
        szinesben('Fénysugár szög: ', egy.geometries[0].geometries[0].beam_angle)
    except AttributeError:
        szinesben('Fénysugár szög: ', '-')
    try:
        szinesben('Lámpatípus: ', egy.geometries[0].geometries[0].beam_type.value)
    except AttributeError:
        szinesben('Lámpatípus', '-')
    try:
        szinesben('Színhőmérésklet: ', egy.geometries[0].geometries[0].color_temperature)
    except AttributeError:
        szinesben('Színhőmérséklet', '-')
    try:
        szinesben('Lámpatípus: ', egy.geometries[0].geometries[0].lamp_type.value)
    except AttributeError:
        szinesben('Lámpatípus', '-')
    try:
        szinesben('Fényerő: ', egy.geometries[0].geometries[0].luminous_flux)
    except AttributeError:
        szinesben('Fényerő', '-')
    try:
        szinesben('Fogyasztás: ', egy.geometries[0].geometries[0].power_consumption)
    except:
        szinesben('Fogyasztás', '-')
    print('Változások: ')
    for rev in egy.revisions:
        szinesben('\tDátum: ', rev.date)
        szinesben('\tSzöveg: ', rev.text)
        szinesben('\tFelhasználó ID: ', rev.user_id)
        print('\t', '-' * 60)


for root, dirs, files in os.walk("/Volumes/Macintosh HD/Users/mnte/MALightingTechnology"):
    for file in files:
        if file.endswith('.gdtf'):
            print(root, file)
            gdtfinfo(pygdtf.FixtureType(os.path.join(root, file)))
