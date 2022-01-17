import pygdtf

egy = pygdtf.FixtureType('./par64.gdtf')
print('Név: ', egy.name)
print('Geometria: ', egy.geometries)
print('Wheels:', egy.wheels)
print('Models:', egy.models)
print('Filters: ', egy.filters)
print('Color Space: ', egy.color_space)
print('Leírás: ', egy.description)
print('DMX Profil: ', egy.dmx_profiles)
print('Emitters: ', egy.emitters)
print('Lámpa tipus Id: ', egy.fixture_type_id)
print('Hosszú elnevezés: ', egy.long_name)
print('Gyártó: ', egy.manufacturer)
print('Rövid név: ', egy.short_name)


