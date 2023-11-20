import inspect
import pygdtf
import os
from termcolor import cprint
from colorama import init
from colorama import Fore
from colorama import Style
init(autoreset=True)

def filescan():
    mappa = os.path.expanduser('~')
    if os.name == 'nt':  # Ha Windózban vagyunk
        mappa = "C:/ProgramData/MALightingTechnology/gma3_library/fixturetypes/"
    elif os.name == 'posix':  # Ha Macen vagyunk
        mappa = os.path.join(mappa, 'MALightingTechnology', 'gma3_library', 'fixturetypes')
    fileok = []
    try:
        for root, dirs, files in os.walk(mappa):
            for file in files:
                if file.endswith('.gdtf'):
                    szinesben(root, '/'+file)
                    # gdtfinfo(pygdtf.FixtureType(os.path.join(root, file)))
                    fileok.append(file)
    except AttributeError:
        print('Nem találtam fájlokat ...')
    return fileok,root

def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])


def szinesben(mi, rizsa):
    """
    :param mi: A kiírás definíciója pl. név:
    :param rizsa: A szöveg pl: PAR64
    :return: false
    """
    print(mi, end='')
    cprint(rizsa, 'green')


def getmembers(osztaly):
    for i in inspect.getmembers(osztaly):
        if not i[0].startswith('__'):
            if not inspect.ismethod(i[1]):
                print(i)


def gdtfinfo(egy):
    # egy = pygdtf.FixtureType('./CPMini.gdtf')
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
            print('\t{} - {}  Szín CIE: Y: {}, x {}, y {}'.
                  format(i, egyslot.name, egyslot.color.Y, egyslot.color.x, egyslot.color.y))
            i += 1
    szinesben('Színtér: ', egy.color_space.mode)
    print('DMX módok:')
    dmxinfo = pygdtf.utils.get_dmx_modes_info(egy)
    for i in dmxinfo:
        ki = ('\t Mód: {} - Név: {} - DMX csatorna számok: {}'.
              format(i.get('mode_id'), i.get('mode_name'), i.get('mode_dmx_channel_count')))
        print(ki)

        #  print(dmxinfo)
        DmxChanInfo = pygdtf.utils.get_dmx_channels(egy, i.get('mode_name'))
        #  print(DmxChanInfo)
        for egycsat in DmxChanInfo:
            for param in egycsat:
                print('\t\tDMX cím: {} - Azononsító: {}'.format(param.get('dmx'), param.get('id')))
    """
    for mod in egy.dmx_modes:
        szinesben('\tMód: ', '{}, attribútumok szám: {}'.format(mod.name, len(mod.dmx_channels)))
        for i in range(0, len(mod.dmx_channels)):
            dmxchs = mod.dmx_channels[i].logical_channels[0].attribute
            szinesben('\t\t{}. Channel: '.format(i+1), dmxchs)
    """
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

if __name__ == '__main__':
    fileok,root = filescan()
    menu = {}
    i = 0
    for egyfile in fileok:
        menu[i] = egyfile
        i += 1
    menu[len(menu)] = 'Kilépés.'
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Melyiket nézzük: '))
        except IndexError:
            print('Nem találok ilyen számot ...')
        if option == len(menu)-1:
            exit(0)
        if option < len(menu):
            gdtfinfo(pygdtf.FixtureType(root+'/'+fileok[option]))
        else:
            cprint('Nem találok ilyen számú elemet ...', 'red')
    """cuccz = (dir(pygdtf))
    i = 0
    for egyitem in cuccz:
        print('{}; {}'.format(i,egyitem))
        i += 1"""