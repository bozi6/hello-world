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
    szinesben('Leírás: ', egy.description)
    szinesben('Gyártó: ', egy.manufacturer)
    print('Tárcsák:')
    tar = egy.wheels
    i = 0
    for slot in tar:
        for egyslot in slot.wheel_slots:
            szinesben('\t{}'.format(i), ' - {} '.format(egyslot.name))

            # szinesben('\t\tSzín IEC: ', 'x: {}, Y: {}, y: {}, z: {}'.format(egyslot.color.x, egyslot.color.Y,
            # egyslot.color.y, egyslot.color.z))
            i += 1
    szinesben('Színtér: ', egy.color_space.mode)
    print('DMX módok:')
    for mod in egy.dmx_modes:
        szinesben('\tMód: ', '{}, attribútumok szám: {}'.format(mod.name, len(mod.dmx_channels)))
        for i in range(0, len(mod.dmx_channels)):
            dmxchs = mod.dmx_channels[i].logical_channels[0].attribute
            szinesben('\t\t{}. Channel: '.format(i+1), dmxchs)
    szinesben('Lámpatípus Id: ', egy.fixture_type_id)
    feny = pygdtf.GeometryBeam()
    szinesben('Fényforrás típusa: ', feny.beam_type)
    szinesben('Fénysugár szög: ', '{}°'.format(feny.beam_angle))
    szinesben('Fogyasztás: ', '{}W'.format(feny.power_consumption))
    szinesben('Színhőmérséklet: ', '{}K'.format(feny.color_temperature))
    szinesben('Fényerő: ','{}LUX'.format(feny.luminous_flux))
    """print('Változások: ')
    for rev in egy.revisions:
        szinesben('\tDátum: ', rev.date)
        szinesben('\tSzöveg: ', rev.text)
        szinesben('\tFelhasználó ID: ', rev.user_id)
        print('\t', '-' * 60)
    """


mappa = os.path.expanduser('~')
if os.name == 'nt':
    mappa = "C:/ProgramData/MALightingTechnology/gma3_library/fixturetypes/"
elif os.name == 'posix':
    mappa = os.path.join(mappa, 'MALightingTechnology', 'gma3_library', 'fixturetypes')
fileok = []
try:
    for root, dirs, files in os.walk(mappa):
        for file in files:
            if file.endswith('.gdtf'):
                print('-' * 80)
                print(root, file)
                print('-' * 80)
                gdtfinfo(pygdtf.FixtureType(os.path.join(root, file)))
                fileok.append(file)
except AttributeError:
    print('Valami fos van...')
    for file in fileok:
        print('- {}'.format(file))
