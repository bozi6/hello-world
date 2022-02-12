import pygdtf
import sys
from termcolor import colored, cprint


def szinesben(mi, rizsa):
    print(mi, end='')
    cprint(rizsa, 'green')


egy = pygdtf.FixtureType('./par64.gdtf')
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
szinesben('Fénysugár szög: ', egy.geometries[0].geometries[0].beam_angle)
szinesben('Lámpatípus: ', egy.geometries[0].geometries[0].beam_type.value)
szinesben('Színhőmérésklet: ', egy.geometries[0].geometries[0].color_temperature)
szinesben('Lámpatípus: ', egy.geometries[0].geometries[0].lamp_type.value)
szinesben('Fényerő: ', egy.geometries[0].geometries[0].luminous_flux)
szinesben('Fogyasztás: ', egy.geometries[0].geometries[0].power_consumption)
print('Változások: ')
for rev in egy.revisions:
    szinesben('\tDátum: ', rev.date)
    szinesben('\tSzöveg: ', rev.text)
    szinesben('\tFelhasználó ID: ', rev.user_id)
    print('\t', '-' * 60)
