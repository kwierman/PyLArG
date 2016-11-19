import xml.etree.ElementTree as ET
from .geometry import *
import exceptions
import logging
from math import pi


class ParsingException(exceptions.Exception):
    pass


class Reader:
    logger = logging.getLogger("GDMLReader")

    def __init__(self, filename):
        tree = ET.parse(filename)
        self.root = tree.getroot()
        try:
            self.definitions = self.root.find('define')
            self.structure = self.root.find('structure')
            self.materials = self.root.find('materials')
            self.solids = self.root.find('solids')
            self.setup = self.root.find('setup')
        except:
            raise ParsingException("Not a properly formatted GDML File")

    @classmethod
    def parse_three_vector(cls, element):
        if element is None:
            #cls.logger.warning("3-Vector Queried in None Element")
            return None
        unit=1.0
        if "unit" in element.attrib:
            if 'deg' in element.attrib['unit']:
                unit=1.0
            elif 'rad' in element.attrib['unit']:
                unit = 180.0/pi
            elif 'cm' in element.attrib['unit']:
                unit = 1.0
            elif 'm' in element.attrib['unit']:
                unit=100.0
            elif 'mm' in element.attrib['unit']:
                unit=0.1
            else:
                self.logger.warning("Unknown Unit: "+element.attrib['unit'])
        return [float(element.attrib['x'])*unit,
                float(element.attrib['y'])*unit,
                float(element.attrib['z'])*unit]

    def process_material(self, element):
        if element is None:
            self.logger.warning("MaterialRef Not Found")
        return None

    def process_boolean(self, element, geo):
        first = element.find('first')
        first_name = first.attrib['ref']
        first_vol = self.solids.find("*[@name='{}']".format(first_name))
        geo.first = self.process_solid(first_vol)

        second = element.find('second')
        second_name = second.attrib['ref']
        second_vol = self.solids.find("*[@name='{}']".format(
            second_name))
        geo.second = self.process_solid(first_vol)
        #get the first, the second , the rotation and the position
        try:
            rotation = element.find('rotation')
            geo.rotation = self.parse_three_vector(rotation)
        except:
            pass
        try:
            position = element.find('position')
            geo.position = self.parse_three_vector(position)
        except:
            pass
        return geo

    def process_union(self, element):
        union = Union()
        self.process_boolean(element, union)
        return union

    def process_subtraction(self, element):
        subtraction = Subtraction()
        self.process_boolean(element, subtraction)
        return subtraction

    def process_intersection(self, element):
        intersection = Intersection()
        self.process_boolean(element, intersection)
        return intersection

    def process_solid(self, element):
        if element is None:
            self.logger.warning("SolidRef Not Found")
            return None
        tag = element.tag
        if tag == "box":
            return Box(self.parse_three_vector(element))
        elif tag == 'tube':
            rmin = 0.0
            if 'rmin' in element.attrib:
                rmin = float(element.attrib['rmin'])
            startphi = 0.0
            if 'startphi' in element.attrib:
                startphi = float(element.attrib['startphi'])
            deltaphi = 360
            if 'deltaphi' in element.attrib:
                deltaphi = float(element.attrib['deltaphi'])
            return Tube(
                rmin,
                float(element.attrib['rmax']),
                deltaphi,
                startphi,
                float(element.attrib['z'])
            )
        elif tag == 'union':
            return self.process_union(element)
        elif tag == 'intersection':
            return self.process_intersection(element)
        elif tag == 'subtraction':
            return self.process_subtraction(element)
        else:
            self.logger.warning("Encountered Unknown Solid: " + tag)
        return None

    def process_phys_vol(self, element):
        position = element.find('position')
        positionref = element.find('positionref')

        rotation = element.find('rotation')
        rotationref = element.find('rotationref')

        volume = element.find("volumeref")
        solid = element.find("solidref")

        if position is not None and positionref is not None:
            self.logger.warning("""Both position and ref defined.
            Parent Element: {}
            Defaulting to position
            """.format(volume.attrib['ref']))
        elif positionref is not None:
            posname = positionref.attrib['ref']
            position = self.solids.find("*position[@name='{}']".format(
                posname))

        if rotation is not None and rotationref is not None:
            self.logger.warning("""Both rotation and ref defined.
            Parent Element: {}
            Defaulting to rotation
            """.format(volume.attrib['ref']))
        elif rotationref is not None:
            rotname = rotationref.attrib['ref']
            rotation = self.solids.find("*rotation[@name='{}']".format(
                rotname))

        if volume is not None and solid is not None:
            self.logger.warning("Both Volume and Solid ref defined")
            self.logger.warning("Volume: {}, Solid: {}".format(
                volume.attrib['ref'], solid.attrib['ref']))

        elif volume is not None and solid is None:
            pos = self.parse_three_vector(position)
            rot = self.parse_three_vector(rotation)
            vol = self.structure.find("volume[@name='{}']".format(
                volume.attrib['ref']))
            return self.parse_volume(vol,pos,rot)

        elif volume is None and solid is not None:
            vol = Volume(element.attrib['name'], position, rotation)
            sol = self.solids.find("*[@name='{}']".format(solid.attrib['ref']))
            vol.solid = self.process_solid(sol)
            return vol
        else:
            logger.error("WARNING, Bottom-Level Element Without Defined Solid")

    def parse_volume(self, element, position=None, rotation=None):
        vol = Volume(element.attrib['name'], position, rotation)
        vol.material = self.process_material(element.find("materialref"))
        solidref = element.find('solidref').attrib['ref']
        solid_element = self.solids.find("*[@name='{}']".format(solidref))
        vol.solid = self.process_solid(solid_element)
        for child in element.findall("physvol"):
            vol.children.append(self.process_phys_vol(child))
        return vol

    def create_geometry(self):
        world = self.setup.find("world")
        world_name = world.attrib['ref']
        self.logger.debug("Creating New Geometry With Name: "+world_name)
        world_volume = self.structure.find("volume[@name='{}']".format(
            world_name))
        return self.parse_volume(world_volume)
