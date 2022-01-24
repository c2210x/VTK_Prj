from vtkmodules.vtkCommonCore import vtkObject
from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkPolyDataMapper,
    vtkRenderWindowInteractor
)
import vtkmodules.vtkRenderingOpenGL2

source = vtkConeSource()

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(source.GetOutputPort())   #设置mapper数据源

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.7, 0.7, 0.7)

renderer = vtkRenderer()   #渲染器
renderer.AddActor(actor)
renderer.SetBackground(0.9, 0.9, 0.9)

window = vtkRenderWindow()
window.AddRenderer(renderer)
window.SetSize(900, 600)
window.Render()

interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactor.SetInteractorStyle(vtkInteractorStyleTrackballCamera())   #设置交互方式
interactor.Initialize()  
interactor.Start()