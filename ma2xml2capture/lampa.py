import uuid


class Lampa:

    def __init__(self, name):
        self.Fixture = name
        self.Optics = '18°'
        self.Wattage = '500w'
        self.Unit = name
        self.Circuit = ''
        self.Channel = '1'
        self.Groups = ''
        self.Patch = '1'
        self.dmxmode = '1'
        self.dmxchannels = '1'
        self.Layer = 'Default Layer'
        self.Focus = ''
        self.Filters = ''
        self.Gobos = ''
        self.Accessories = ''
        self.Purpose = ''
        self.Note = 'Megjegyzés'
        self.Weight = '5.0kg'
        self.Location = 'Location'
        self.posx = {'x': '0'}
        self.posy = {'y': '0'}
        self.posz = {'z': '0'}
        self.rotx = {'x': '0°'}
        self.roty = {'y': '0°'}
        self.rotz = {'z': '0°'}
        self.focus = '0°'
        self.pan = '0°'
        self.focustilt = '0°'
        self.invertpan = 'No'
        self.panstartlimit = '0'
        self.panendlimit = '0'
        self.inverttilt = 'No'
        self.tiltstartlim = '0°'
        self.tiltendlim = '0°'
        self.Identifier = uuid.uuid4()
        self.extidentifier = ''

    def __repr__(self):
        return '<Lamp object. Name: {}>'.format(self.Fixture)

    def showlampa(self):
        for kulcs in self.__dict__.keys():
            print(kulcs, self.__dict__[kulcs])
        print('Lámpainformációk:')
        print('\tNév:', self.Fixture)
        print('\tOptika:', self.Optics)
        print('\tTeljesítmény:', self.Wattage)
        print('\tEgység:', self.Unit)
        print('\tÁramkör:', self.Circuit)
        print('\tCsatorna:', self.Channel)
        print('\tCsoport:', self.Groups)
        print('\tPatch:', self.Patch)
        print('\tDMX mód:', self.dmxmode)
        print('\tDMX csatornák:', self.dmxchannels)
        print('\tRéteg:', self.Layer)
        print('\tFókusz:', self.Focus)
        print('\tFilter:', self.Filters)
        print('\tGobók:', self.Gobos)
        print('\tAccessories:', self.Accessories)
        print('\tPurpose:', self.Purpose)
        print('\tMegjegyzés:', self.Note)
        print('\tTömeg:', self.Weight)
        print('\tElhelyezkedés:', self.Location)
        print('\tX pozíció:', self.posx)
        print('\tY pozíció:', self.posy)
        print('\tZ pozíció:', self.posz)
        print('\tX forgatás:', self.rotx)
        print('\tY forgatás:', self.roty)
        print('\tZ forgatás:', self.rotz)
        print('\tFókusz:', self.focus)
        print('\tPan:', self.pan)
        print('\tFókusz tilt:', self.focustilt)
        print('\tInvert Pan:', self.invertpan)
        print('\tPan Start Limit:', self.panstartlimit)
        print('\tPan End Limit:', self.panendlimit)
        print('\tInvert Tilt:', self.inverttilt)
        print('\tTilt Start Limit:', self.tiltstartlim)
        print('\tTilt End Limit:', self.tiltendlim)
        print('\tIdentifier:', self.Identifier)
        print('\tExternal Identifer:', self.extidentifier)

    def lamplista(self):
        lista = (self.Fixture, self.Optics, self.Wattage, self.Unit, self.Circuit, self.Channel, self.Groups,
                 self.Patch, self.dmxmode, self.dmxchannels, self.Layer, self.Focus, self.Filters, self.Gobos,
                 self.Accessories, self.Purpose, self.Note, self.Weight, self.Location, self.posx, self.posy,
                 self.posz, self.rotx, self.roty, self.rotz, self.Focus, self.pan, self.focustilt, self.invertpan,
                 self.panstartlimit, self.panendlimit, self.inverttilt, self.tiltstartlim, self.tiltendlim,
                 self.Identifier, self.extidentifier)
        return lista
