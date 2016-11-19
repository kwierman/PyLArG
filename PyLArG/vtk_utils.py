import vtk
import logging
from .geometry import *
import exceptions
from math import pi

class WritingError(exceptions.Exception):
    pass

class Writer:
    logger = logging.getLogger("VTKWriter")

    def __init__(self, filename):
        self.writer = vtk.vtkXMLPolyDataWriter();
        self.writer.SetFileName(filename);
        self.appendpolydata = vtk.vtkAppendPolyData()

    def apply_transformations(self, geo, position, rotation):
        transform = vtk.vtkTransform()
        if position is not None:
            transform.Translate(position[0],position[1],position[2])
        if rotation is not None:
            transform.RotateX(rotation[0])
            transform.RotateY(rotation[1])
            transform.RotateZ(rotation[2])

        transform_filter = vtk.vtkTransformFilter()
        transform_filter.SetTransform(transform)
        transform_filter.SetInputConnection(geo)
        transform_filter.Update()
        self.logger.debug("Applying Transformation")
        return transform_filter

    def write_box(self, box, position, rotation):
        vtk_box = vtk.vtkCubeSource()
        vtk_box.SetXLength(box.pos[0])
        vtk_box.SetYLength(box.pos[1])
        vtk_box.SetZLength(box.pos[2])
        #vtk_box.SetCenter(position[0],position[1],position[2])
        vtk_box.Update()
        data = self.apply_transformations(vtk_box.GetOutputPort(), position, rotation)
        self.logger.debug("Writing Box")
        return data

    def write_tube(self, tube, position, rotation):
        diskSource = vtk.vtkDiskSource()
        diskSource.SetInnerRadius(tube.rmin)
        diskSource.SetOuterRadius(tube.rmax)
        circumfrence = 2*pi*tube.rmax # now in cm.

        diskSource.SetCircumferentialResolution(int(circumfrence))
        diskSource.Update()
        #TODO deltaphi and startphi

        #extrude
        linearExtrusion = vtk.vtkLinearExtrusionFilter()
        linearExtrusion.SetInputConnection(diskSource.GetOutputPort())
        linearExtrusion.SetExtrusionTypeToNormalExtrusion()
        linearExtrusion.SetVector(0,0,1)
        linearExtrusion.SetScaleFactor(tube.z)
        linearExtrusion.Update()

        data = self.apply_transformations(linearExtrusion.GetOutputPort(), position, rotation)
        self.logger.debug("Writing Tube")
        return data

    def write_sphere(self, sphere, position, rotation):
        sphereSource = vtk.vtkSphereSource()
        sphereSource.SetRadius(sphere.rmax)
        sphereSource.SetCenter(position[0],position[1], position[2])
        data = self.apply_transformations(sphereSource.GetOutputPort(), position, rotation)
        self.logger.debug("Writing Sphere")
        return data

    def write_boolean_operation(self, obj, position, rotation, operation):
        #TODO: Stop these shenanigans
        return None
        logging.debug("Writing Boolean Object {} : {}, {}".format(
            obj.__class__.__name__,
            obj.first.__class__.__name__,
            obj.second.__class__.__name__
        ) )
        booleanFilter = vtk.vtkBooleanOperationPolyDataFilter()
        input1 = None
        input2 = None

        if isinstance(obj.first, Box):
            input1 = self.write_box(obj.first, position, rotation)
        elif isinstance(obj.first, Tube):
            input1 = self.write_tube(obj.first, position, rotation)
        elif isinstance(obj.first, Sphere):
            input1 = self.write_sphere(obj.first, position, rotation)
        elif isinstance(obj.first, Union):
            input1 = self.write_union(obj.first, position, rotation)
        elif isinstance(obj.first, Subtraction):
            input1 = self.write_intersection(obj.first, position, rotation)
        elif isinstance(obj.first, Intersection):
            input1 = self.write_union(obj.first, position, rotation)
        else:
            self.logger.warning("Encountered Unknown Type: {}".format(obj.first.__class__.__name__))
            raise WritingError("Unkown Type Encountered in Boolean First")
        if input1 is None:
            self.logger.warning("Input1 is Null for "+obj.first.__class__.__name__)

        if isinstance(obj.second, Box):
            input2 = self.write_box(obj.second, position, rotation)
        elif isinstance(obj.second, Tube):
            input2 = self.write_tube(obj.second, position, rotation)
        elif isinstance(obj.second, Sphere):
            input2 = self.write_sphere(obj.second, position, rotation)
        elif isinstance(obj.second, Union):
            input2 = self.write_union(obj.second, position, rotation)
        elif isinstance(obj.second, Subtraction):
            input2 = self.write_intersection(obj.second, position, rotation)
        elif isinstance(obj.second, Intersection):
            input2 = self.write_union(obj.second, position, rotation)
        else:
            self.logger.warning("Encountered Unknown Type: {}".format(obj.second.__class__.__name__))
            raise WritingError("Unknown Type Encoutered in Boolean Second")
        if input2 is None:
            self.logger.warning("Input2 is Null for "+ obj.second.__class__.__name__)

        if(input1 is None or input2 is None):
            return None

        #if isinstance(obj.first, Box) or isinstance(obj.first, Tube) or isinstance(obj.first, Sphere):
        tmp = vtk.vtkTriangleFilter()
        tmp.SetInputConnection(input1.GetOutputPort())
        tmp.Update()
        input1 = tmp

        #if isinstance(obj.second, Box) or isinstance(obj.second, Tube) or isinstance(obj.second, Sphere):
        tmp = vtk.vtkTriangleFilter()
        tmp.SetInputConnection(input2.GetOutputPort())
        tmp.Update()
        input2 = tmp

        #So, here, the trick
        transformed_surface = self.apply_transformations(input2.GetOutputPort(), obj.position, obj.rotation)

        if vtk.VTK_MAJOR_VERSION <= 5:
            booleanFilter.SetInputConnection( 0, input1.GetProducerPort() )
            booleanFilter.SetInputConnection( 1, input2.GetProducerPort() )
        else:
            booleanFilter.SetInputData( 0, input1.GetOutputDataObject(0) )
            booleanFilter.SetInputData( 1, transformed_surface.GetOutputDataObject(0) )

        self.logger.debug("Applying Boolean Filter")
        try:
            booleanFilter.SetTolerance(1.0)
            booleanFilter.SetOperation(operation)
            booleanFilter.Update()
            self.logger.debug("Finished Creating Boolean Surface")
            return self.apply_transformations(booleanFilter.GetOutputPort(), rotation, position)
        except:
            self.logger.warning("Failed")
            return None

    def write_union(self, union, position, rotation):
        operation = 0
        return self.write_boolean_operation(union, position, rotation, operation)

    def write_intersection(self, union, position, rotation):
        operation = 1
        return self.write_boolean_operation(union, position, rotation, operation)

    def write_subtraction(self, union, position, rotation):
        operation = 2
        return self.write_boolean_operation(union, position, rotation, operation)

    def write_subgeometry(self, geometry, external_position, external_rotation):
        position = [i + external_position[index] for index, i in enumerate(geometry.position)]
        rotation = [i + external_rotation[index] for index, i in enumerate(geometry.rotation)]
        #position = geometry.position
        #rotation = geometry.rotation
        solid = geometry.solid
        data = None
        if isinstance(solid, Box):
            data = self.write_box(solid, position, rotation)
        elif isinstance(solid, Tube):
            data = self.write_tube(solid, position, rotation)
        elif isinstance(solid, Sphere):
            data = self.write_sphere(solid, position, rotation)
        elif isinstance(solid, Union):
            data = self.write_union(solid, position, rotation)
        elif isinstance(solid, Subtraction):
            data = self.write_intersection(solid, position, rotation)
        elif isinstance(solid, Intersection):
            data = self.write_union(solid, position, rotation)
        else:
            self.logger.warning("Encountered Unknown Type: {}".format(solid.__class__.__name__))
        if data is not None:
            self.logger.debug("Writing SubGeometry: "+str(data))
            self.appendpolydata.AddInputData(data.GetOutput())
            self.appendpolydata.Update()
        else:
            self.logger.warning("Received no data from Object: "+solid.__class__.__name__)
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
