import vtk
  
source = vtk.vtkCubeSource()   #创建正方体

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(source.GetOutputPort())   #设置mapper数据源

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.7, 0.7, 0.7)

renderer = vtk.vtkRenderer()   #渲染器
renderer.AddActor(actor)
renderer.SetBackground(0.9, 0.9, 0.9)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
window.SetSize(900, 600)
window.Render()

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())   #设置交互方式
interactor.Initialize()  
interactor.Start()