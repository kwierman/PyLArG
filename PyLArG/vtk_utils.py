import vtk
import logging
from .geometry import *

class Writer:
    logger = logging.getLogger("VTKWriter")

    def __init__(self, filename):
        self.writer = vtk.vtkXMLPolyDataWriter();
        self.writer.SetFileName(filename);
        self.appendpolydata = vtk.vtkAppendPolyData()

    def apply_transformations(self, geo, position, rotation):
        transform = vtk.vtkTransform()
        transform.Translate(position[0],position[1],position[2])
        transform.RotateWXYZ(rotation[0], [1,0,0])
        transform.RotateWXYZ(rotation[1], [0,1,0])
        transform.RotateWXYZ(rotation[2], [0,0,1])

        transform_filter = vtk.vtkTransformFilter()
        transform_filter.SetTransform(transform)
        transform_filter.SetInputConnection(geo.GetOutputPort())
        transform_filter.Update()

        polydata = vtk.vtkPolyData()
        polydata.ShallowCopy(transform_filter.GetOutput())
        self.appendpolydata.AddInputData(polydata)
        self.appendpolydata.Update()

    def write_box(self, box, position, rotation):
        vtk_box = vtk.vtkCubeSource()
        vtk_box.SetXLength(box.pos[0])
        vtk_box.SetYLength(box.pos[1])
        vtk_box.SetZLength(box.pos[2])
        #vtk_box.SetCenter(position[0],position[1],position[2])
        vtk_box.Update()
        self.apply_transformations(vtk_box, position, rotation)


    def write_tube(self, tube, position, rotation):
        diskSource = vtk.vtkDiskSource()
        diskSource.SetInnerRadius(tube.rmin)
        diskSource.SetOuterRadius(tube.rmax)
        diskSource.Update()
        #TODO deltaphi and startphi

        #extrude
        linearExtrusion = vtk.vtkLinearExtrusionFilter()
        linearExtrusion.SetInputConnection(diskSource.GetOutputPort())
        linearExtrusion.SetExtrusionTypeToNormalExtrusion()
        linearExtrusion.SetVector(0,0,tube.z)
        linearExtrusion.Update()

        self.apply_transformations(linearExtrusion, position, rotation)

    def write_subgeometry(self, geometry, external_position, external_rotation):
        #position = [i + external_position[index] for index, i in enumerate(geometry.position)]
        #rotation = [i + external_rotation[index] for index, i in enumerate(geometry.rotation)]
        position = geometry.position
        rotation = geometry.rotation
        solid = geometry.solid
        if isinstance(solid, Box):
            self.write_box(solid, position, rotation)
        elif isinstance(solid, Tube):
            self.write_tube(solid, position, rotation)
        else:
            self.logger.warning("Encountered Unknown Type: {}".format(type(solid)))
        for child in geometry._children:
            self.write_subgeometry(child, position, rotation)

    def write_geometry(self, geometry):
        self.logger.info("Creating PolyData")
        self.write_subgeometry(geometry, [0.0,0.0,0.0], [0.0,0.0,0.0])
        self.logger.info("Finished Creating PolyData")
        if vtk.VTK_MAJOR_VERSION <= 5:
            self.writer.SetInput(self.appendpolydata.GetOutput())
        else:
            self.writer.SetInputData(self.appendpolydata.GetOutput())
        self.writer.SetDataModeToBinary()
        self.writer.Write()
        self.logger.info("Wrote PolyData to File")
