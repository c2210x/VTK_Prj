# from vtkmodules.vtkCommonCore import vtkObject
# from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource, vtkLineSource
# from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkDataSetMapper,
#     vtkRenderer,
#     vtkRenderWindow,
#     vtkPolyDataMapper,
#     vtkRenderWindowInteractor,
#     vtkProperty
# )
# import vtkmodules.vtkRenderingOpenGL2

import vtkmodules.all as vtk
from CmGeomAlgorithm import *

class VTKAdapter:
    def __init__(self, bgClr = (0.95, 0.95, 0.95)):
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(bgClr)
        self.window = vtk.vtkRenderWindow()
        self.window.AddRenderer(self.renderer)
        self.window.SetSize(1000, 1000)
        self.interactor = vtk.vtkRenderWindowInteractor()
        self.interactor.SetRenderWindow(self.window)
        self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.interactor.Initialize()
    def Display(self):
        self.interactor.Start()
    def SetBackGroundColor(self, r, g, b):
        return self.renderer.SetBackground(r, g, b)
    def DrawAxes(self, length = 100, shaftType = 0, cylinderRadius = 0.01, coneRadius = 0.2):
        axes = vtk.vtkAxesActor()
        axes.SetTotalLength(length, length, length)
        axes.SetShaftType(shaftType)
        axes.SetCylinderRadius(cylinderRadius)
        axes.SetConeRadius(coneRadius)
        axes.SetAxisLabels(0)
        self.renderer.AddActor(axes)
    def DrawActor(self, actor):
        self.renderer.AddActor(actor)
        return actor
    def DrawPdSrc(self, pdSrc):
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(pdSrc.GetOutputPort())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        return self.DrawActor(actor)
    def DrawSTLModel(self, stlFilePath):
        reader = vtk.vtkSTLReader()
        reader.SetFileName(stlFilePath)
        return self.DrawPdSrc(reader)
    def RemoveActor(self, actor):
        self.renderer.RemoveActor(actor)
    def DrawPoint(self, point, radius = 2.0):
        src = vtk.vtkSphereSource()
        src.SetCenter(point.x, point.y, point.z)
        src.SetRadius(radius)
        return self.DrawPdSrc(src)
    def DrawSegment(self, seg):
        src = vtk.vtkLineSource()
        src.SetPoint1(seg.A.x, seg.A.y, seg.A.z)
        src.SetPoint2(seg.B.x, seg.B.y, seg.B.z)
        return self.DrawPdSrc(src)
    def DrawPolyline(self, polyline : CmPolyline):
        src = vtk.vtkLineSource()
        points = vtk.vtkPoints()
        for i in range(polyline.GetPointsCount()):
            pt = polyline.GetPointFromIdx(i)
            points.InsertNextPoint((pt.x, pt.y, pt.z))
        src.SetPoints(points)
        return self.DrawPdSrc(src)
    pass

