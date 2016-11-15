import vtk
import logging

class Writer:
    logger = logging.getLogger("VTKWriter")

    def __init__(self, filename):
        print dir(vtk)
        print vtk.__file__
        self.writer = vtk.vtkXMLPolyDataWriter();
        self.writer.SetFileName(filename);
        self.polydata = vtk.vtkPolyData()

    def write_box(self, box):
        vtk_box = vtk.vtkCubeSource(box.pos[0], box.pos[1], box.pos[2])
        self.polydata.SetPolys(vtk_box)

    def write_subgeometry(self, geometry):
        pass

    def write_geometry(self, geometry):
        if vtk.VTK_MAJOR_VERSION <= 5:
            self.writer.SetInput(self.polydata)
        else:
            self.writer.SetInputData(self.polydata)
        self.writer.Write()
