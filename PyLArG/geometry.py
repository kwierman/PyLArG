"""
    Raw Geometry Definitions.
    These are meant to interface between the geometry packages as a
    least common denominator.
    Packages will thus need to define adaptation methods.

"""

class Volume:
    def __init__(self, name, position=None, rotation=None):
        self.name = name
        self._children = []
        self._solid = None
        self._material = None
        if position is None:
            self.position = [0,0,0]
        else:
            self.position = position
        if rotation is None:
            self.rotation = [0,0,0]
        else:
            self.rotation = rotation

    @property
    def children(self):
        return self._children

    @property
    def solid(self):
        return self._solid

    @property
    def material(self):
        return self._material


class Material:
    def __init__(self, name):
        self.name = name
        self._formula = ''
        self._composition ={}

    @property
    def formula(self):
        return self._formula

    @property
    def composition(self):
        return self._composition


class Box:
    def __init__(self, pos):
        self.pos = pos
    def __str__(self):
        return "Box: {}".format(self.pos)

class Tube:
    def __init__(self, rmin, rmax, deltaphi, startphi, z):
        self.rmin = rmin
        self.rmax = rmax
        self.deltaphi = deltaphi
        self.startphi = startphi
        self.z=z
    def __str__(self):
        return "Tube: {},{},{}".format(self.rmin,self.rmax, self.z)

class Sphere:
    def __init__(self, rmin, rmax, deltaphi, startphi, starttheta, deltatheta):
        self.rmin = rmin
        self.rmax = rmax
        self.deltaphi = deltaphi
        self.startphi = startphi
        self.starttheta = starttheta
        self.deltatheta = deltatheta

class Union:
    def __init__(self):
        self.first= None
        self.second = None
        self.position = None
        self.rotation = None

class Intersection:
    def __init__(self):
        self.first = None
        self.second = None
        self.position = None
        self.rotation = None

class Subtraction:
    def __init__(self):
        self.first = None
        self.second = None
        self.position = None
        self.rotation = None
