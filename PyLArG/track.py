from data import *
import vtk

class Reader:
    pass


class Writer:

    def __init__(self, filename):
        self.writer =vtk.vtkXMLPolyDataWriter()
        self.points = vtk.vtkPoints()

    def write(self):
        self.
