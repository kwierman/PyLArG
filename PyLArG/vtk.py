import vtk


class Writer:
    def __init__(self, filename):
        self.writer = vtk.vtkXMLPolyDataWriter();
        self.writer.SetFileName(filename);

    def write_geometry(self, geometry):



        if vtk.VTK_MAJOR_VERSION <= 5:
            self.writer.SetInput(polydata)
        else:
            self.writer.SetInputData(polydata)
        self.writer.Write()
