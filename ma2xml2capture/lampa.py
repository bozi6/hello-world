import uuid


class Lampa:

    def __init__(self, name):
        self.Fixture = name
        self.Optics = '18°'
        self.Wattage = '500w'
        self.Unit = '1'
        self.Circuit = '1'
        self.Channel = '1'
        self.Groups = '1'
        self.Patch = '1'
        self.dmxmode = '1'
        self.dmxchannels = '1'
        self.Layer = 'Default Layer'
        self.Focus = '1'
        self.Filters = '1'
        self.Gobos = '1'
        self.Accessories = '1'
        self.Purpose = '1'
        self.Note = 'Megjegyzés'
        self.Weight = '5.0kg'
        self.Location = 'hol a lámpa'
        self.posx = {'x': '0'}
        self.posy = {'y': '0'}
        self.posz = {'z': '0'}
        self.rotx = {'x': '0°'}
        self.roty = {'y': '0°'}
        self.rotz = {'z': '0°'}
        self.focus = ''
        self.pan = ''
        self.focustilt = ''
        self.invertpan = 'No'
        self.panstartlimit = '0'
        self.panendlimit = '0'
        self.inverttilt = 'No'
        self.tiltstartlim = '0'
        self.tiltendlim = '0'
        self.Identifier = ''
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
        print('\tRéteg:', self.layer)
        print('\tFókusz:', self.focus)
        print('\tFilter:', self.filters)
        print('\tGobók:', self.gobos)
        print('\tAccessories:', self.accessories)
        print('\tPurpose:', self.purpose)
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
        print('\tIdentifier:', self.identifier)
        print('\tExternal Identifer:', self.extidentifier)
