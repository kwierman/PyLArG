import vtk
import logging
from .geometry import *
import exceptions
from math import pi

class WritingError(exceptions.Exception):
    pass

class Writer:
    logger = logging.getLogger("VTK::Writer")
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
        vtk_box.SetCenter(0,0,0)
        vtk_box.Update()

        data = self.apply_transformations(vtk_box.GetOutputPort(), position, rotation)
        self.logger.debug("Writing Box")
        return data

    def write_tube(self, tube, position, rotation):
        diskSource = vtk.vtkDiskSource()
        diskSource.SetInnerRadius(tube.rmin)
        diskSource.SetOuterRadius(tube.rmax)
        circumfrence = 2*pi*tube.rmax # now in cm.

        diskSource.SetCircumferentialResolution(100)
        diskSource.Update()

        linearExtrusion = vtk.vtkLinearExtrusionFilter()
        linearExtrusion.SetInputConnection(diskSource.GetOutputPort())
        linearExtrusion.SetExtrusionTypeToNormalExtrusion()
        linearExtrusion.SetVector(0,0,1)
        linearExtrusion.SetScaleFactor(tube.z)
        linearExtrusion.Update()

        implicit_transform =self.apply_transformations(linearExtrusion.GetOutputPort(),
            [0,0,-tube.z/2.],[0,0,0])

        data = self.apply_transformations(implicit_transform.GetOutputPort(),
                                          position, rotation)
        self.logger.debug("Writing Tube")
        return data

    def write_sphere(self, sphere, position, rotation):
        sphereSource = vtk.vtkSphereSource()
        sphereSource.SetRadius(sphere.rmax)
        sphereSource.SetCenter(position[0],position[1], position[2])
        data = self.apply_transformations(sphereSource.GetOutputPort(), position, rotation)
        self.logger.debug("Writing Sphere")
        return data

    def check_intersection(self, input1, input2):
        self.logger.debug("Checking Intersection")
        bounds1 = [0.,0.,0.,0.,0.,0.]
        bounds2 = [0.,0.,0.,0.,0.,0.]
        input1.GetOutput().GetBounds(bounds1)
        input2.GetOutput().GetBounds(bounds2)
        self.logger.debug(bounds1)
        self.logger.debug(bounds2)

        #if input2 is inside input1 (assume squares)
        if bounds1[0]<=bounds2[0]<=bounds1[1] and bounds1[0]<=bounds2[1]<=bounds1[1]:
            if bounds1[2]<=bounds2[2]<=bounds1[3] and bounds1[2]<=bounds2[3]<=bounds1[3]:
                if bounds1[4]<=bounds2[4]<=bounds1[5] and bounds1[4]<=bounds2[5]<=bounds1[5]:
                    return False

        #if input2 is inside input1 (assume squares)
        if bounds2[0]<=bounds1[0]<=bounds2[1] and bounds2[0]<=bounds1[1]<=bounds2[1]:
            if bounds2[2]<=bounds1[2]<=bounds2[3] and bounds2[2]<=bounds1[3]<=bounds2[3]:
                if bounds2[4]<=bounds1[4]<=bounds2[5] and bounds2[4]<=bounds1[5]<=bounds2[5]:
                    return False

        return True

    def write_boolean_operation(self, obj, position, rotation, operation):
        return None
        self.logger.debug("Writing Boolean Object {}".format(
            obj.__class__.__name__
        ) )
        self.logger.debug("First: {}".format(obj.first))
        self.logger.debug("Second: {}".format(obj.second))
        self.logger.debug("Rotation: {}".format(obj.rotation))
        self.logger.debug("Position: {}".format(obj.position))

        booleanFilter = vtk.vtkBooleanOperationPolyDataFilter()
        booleanFilter.SetOperation(operation)
        input1 = None
        input2 = None

        if isinstance(obj.first, Box):
            input1 = self.write_box(obj.first, [0,0,0], [0,0,0])
        elif isinstance(obj.first, Tube):
            input1 = self.write_tube(obj.first, [0,0,0], [0,0,0])
        elif isinstance(obj.first, Sphere):
            input1 = self.write_sphere(obj.first, [0,0,0], [0,0,0])
        elif isinstance(obj.first, Union):
            input1 = self.write_union(obj.first, [0,0,0], [0,0,0])
        elif isinstance(obj.first, Subtraction):
            input1 = self.write_intersection(obj.first, [0,0,0], [0,0,0])
        elif isinstance(obj.first, Intersection):
            input1 = self.write_union(obj.first, [0,0,0], [0,0,0])
        else:
            cls_name = obj.first.__class__.__name__
            self.logger.error("Encountered Unknown Type: " + cls_name)
            raise WritingError("Unkown Type Encountered in Boolean First")
        if input1 is None:
            cls_name = obj.first.__class__.__name__
            self.logger.warning("Input1 is Null for " + cls_name)
        if isinstance(obj.second, Box):
            input2 = self.write_box(obj.second, obj.position, obj.rotation)
        elif isinstance(obj.second, Tube):
            input2 = self.write_tube(obj.second, obj.position, obj.rotation)
        elif isinstance(obj.second, Sphere):
            input2 = self.write_sphere(obj.second, obj.position, obj.rotation)
        elif isinstance(obj.second, Union):
            input2 = self.write_union(obj.second, obj.position, obj.rotation)
        elif isinstance(obj.second, Subtraction):
            input2 = self.write_intersection(obj.second, obj.position, obj.rotation)
        elif isinstance(obj.second, Intersection):
            input2 = self.write_union(obj.second, obj.position, obj.rotation)
        else:
            self.logger.warning("Encountered Unknown Type: {}".format(obj.second.__class__.__name__))
            raise WritingError("Unknown Type Encoutered in Boolean Second")
        if input2 is None:
            self.logger.warning("Input2 is Null for "+ obj.second.__class__.__name__)

        if(input1 is None or input2 is None):
            return None

        tmp1 = vtk.vtkTriangleFilter()
        tmp1.SetInputConnection(input1.GetOutputPort())
        tmp1.Update()
        input1 = tmp1

        tmp2 = vtk.vtkTriangleFilter()
        tmp2.SetInputConnection(input2.GetOutputPort())
        tmp2.Update()
        input2 = tmp2

        self.appendpolydata.AddInputData(self.apply_transformations(input1.GetOutputPort(), rotation, position).GetOutput())
        self.appendpolydata.Update()
        self.appendpolydata.AddInputData(self.apply_transformations(input2.GetOutputPort(), rotation, position).GetOutput())
        self.appendpolydata.Update()
        return None

        booleanFilter.SetInputData(0, self.apply_transformations(input1.GetOutputPort(), rotation, position).GetOutput())
        booleanFilter.SetInputData(1, self.apply_transformations(input2.GetOutputPort(), rotation, position).GetOutput())

        if not self.check_intersection(input1, input2):
            self.logger.warning("Could NOT find intersection")
            return None
        self.logger.debug("Found Intersections")

        self.logger.debug("Applying Boolean Filter")
        try:
            booleanFilter.SetTolerance(1.e-12)
            booleanFilter.Update()
            self.logger.debug("Finished Creating Boolean Surface")
            return booleanFilter
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
        self.logger.debug("Processing Subgeometry: "+geometry.name)
        position = [i + external_position[index] for index, i in enumerate(geometry.position)]
        rotation = [i + external_rotation[index] for index, i in enumerate(geometry.rotation)]
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
            self.logger.debug("Writing SubGeometry: "+geometry.__class__.__name__)
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
        self.writer.SetInputData(self.appendpolydata.GetOutput())
        self.writer.SetDataModeToBinary()
        self.writer.Write()
        self.logger.info("Wrote PolyData to File")
