# Raw Geometry definitions
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
