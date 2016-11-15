from PyLArG.gdml import Reader
from PyLArG.vtk import Writer
import argparse
import logging
logging.basicConfig(level = logging.DEBUG)

parser = argparse.ArgumentParser(description='Process Some Geometry.')
parser.add_argument('input_geometry', metavar='input', type=str,
                    help='The input GDML')

args = parser.parse_args()
gdml_parser = Reader(args.input_geometry)
geometry = gdml_parser.create_geometry()
writer = Writer(args.input_geometry.replace('.gdml','.vtk'))
writer.write_geometry(geometry)
