import vtk
import logging
from .geometry import *

class Writer:
    logger = logging.getLogger("VTKWriter")

    def __init__(self, filename):
        self.writer = vtk.vtkXMLPolyDataWriter();
        self.writer.SetFileName(filename);
        self.appendpolydata = vtk.vtkAppendPolyData()
        self.polydata = []
        self.objects=[]

    def write_box(self, box, position):
        self.logger.debug("Writing Box")
        self.logger.debug("Lengths {}".format(box.pos))
        self.logger.debug("Position {}".format(position))
        vtk_box = vtk.vtkCubeSource()
        vtk_box.SetXLength(box.pos[0])
        vtk_box.SetYLength(box.pos[1])
        vtk_box.SetZLength(box.pos[2])
        vtk_box.SetCenter(position[0],position[1],position[2])
        vtk_box.Update()
        polydata = vtk.vtkPolyData()
        polydata.ShallowCopy(vtk_box.GetOutput())
        self.appendpolydata.AddInputData(polydata)
        self.polydata.append(polydata)
        self.appendpolydata.Update()
        #self.assembly.ShallowCopy
        #self.writer.SetInputConnection(vtk_box.GetOutputPort())
        self.objects.append(vtk_box)

    def write_subgeometry(self, geometry):
        position = geometry.position
        solid = geometry.solid
        if isinstance(solid, Box):
            self.write_box(solid, position)
        else:
            self.logger.warning("Encountered Unknown Type: {}".format(type(solid)))
        for child in geometry._children:
            self.write_subgeometry(child)

    def write_geometry(self, geometry):
        self.write_subgeometry(geometry)
        self.logger.info("Finished Creating PolyData")
        if vtk.VTK_MAJOR_VERSION <= 5:
            self.writer.SetInput(self.appendpolydata.GetOutput())
        else:
            self.writer.SetInputData(self.appendpolydata.GetOutput())
        self.writer.SetDataModeToBinary()
        self.writer.Write()
