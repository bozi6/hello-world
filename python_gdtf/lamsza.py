import inspect
import pygdtf
import os
from termcolor import cprint
from colorama import init
init(autoreset=True)


def szinesben(mi, rizsa):
    print(mi, end='')
    cprint(rizsa, 'green')


def getmembers(osztaly):
    for i in inspect.getmembers(osztaly):
        if not i[0].startswith('__'):
            if not inspect.ismethod(i[1]):
                print(i)


def gdtfinfo(egy):
    # egy = pygdtf.FixtureType('./par64.gdtf')
    szinesben('Név: ', egy.name)
    szinesben('Rövid név: ', egy.short_name)
    szinesben('Hosszú név: ', egy.long_name)
    print('Tárcsák:')
    for item in egy.wheels:
        szinesben('\tNév:', item.name)
    print('Színek tárcsán:')
    for item in egy.filters:
        szinesben('\tNév: ', item.name)
    szinesben('Színtér: ', egy.color_space.mode)
    szinesben('Leírás: ', egy.description)
    szinesben('DMX Profil: ', egy.dmx_profiles)
    szinesben('Lámpatípus Id: ', egy.fixture_type_id)
    szinesben('Gyártó: ', egy.manufacturer)
    for geom in egy.geometries:
        print("Ezmiafasz!: ", geom.power_consumption)

    try:
        szinesben('Fényvető típusa: ', egy.geometries[0].geometries[0].beam_type.value)
    except AttributeError:
        szinesben('Fényvető típusa:', ' -')
    try:
        szinesben('Színhőmérésklet: ', egy.geometries[0].geometries[0].color_temperature)
    except AttributeError:
        szinesben('Színhőmérséklet', ' -')
    try:
        szinesben('Lámpatípus: ', egy.geometries[0].geometries[0].lamp_type.value)
    except AttributeError:
        szinesben('Lámpatípus', ' -')
    try:
        szinesben('Fényerő: ', egy.geometries[0].geometries[0].luminous_flux)
    except AttributeError:
        szinesben('Fényerő', ' -')
    try:
        szinesben('Fogyasztás: ', egy.geometries[0].geometries[0].power_consumption)
    except AttributeError:
        szinesben('Fogyasztás', ' -')
    """print('Változások: ')
    for rev in egy.revisions:
        szinesben('\tDátum: ', rev.date)
        szinesben('\tSzöveg: ', rev.text)
        szinesben('\tFelhasználó ID: ', rev.user_id)
        print('\t', '-' * 60)
    """


for root, dirs, files in os.walk("C:/ProgramData/MALightingTechnology/gma3_library/fixturetypes/"):
    for file in files:
        if file.endswith('.gdtf'):
            print(root, file)
            gdtfinfo(pygdtf.FixtureType(os.path.join(root, file)))



