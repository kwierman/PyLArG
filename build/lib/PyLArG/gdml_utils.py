import xml.etree.ElementTree as ET
from .geometry import *
import exceptions
import logging


class ParsingException(exceptions.Exception):
    pass


class Reader:
    logger = logging.getLogger("GDML_READER")

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
    def parse_three_vector(self, element):
        if element is None:
            return None
        return [element.attrib['x'], element.attrib['y'], element.attrib['z']]

    def process_material(self, element):
        if element is None:
            self.logger.warning("MaterialRef Not Found")
        return None

    def process_solid(self, element):
        if element is None:
            self.logger.warning("SolidRef Not Found")

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

        if rotation is not None and rotationref is not None:
            self.logger.warning("""Both rotation and ref defined.
            Parent Element: {}
            Defaulting to rotation
            """.format(volume.attrib['ref']))

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
            vol = Volume(element.attrib['name'])
            sol = self.solids.find("[@name='{}']".format())
            vol.solid = self.process_solid(sol)
            return vol

        else:
            logger.error("WARNING, NO BOTTOM ELEMENT DETECTED")

    def parse_volume(self, element, position=None, rotation=None):
        vol = Volume(element.attrib['name'], position, rotation)
        vol.material = self.process_material(element.find("materialref"))
        vol.solid = self.process_solid(element.find('solidref'))
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
