import vtk

stlReader = vtk.vtkSTLReader()
stlReader.SetFileName("D:\\_Design Software\\Python\\Download_Misc\\STL\\3D.STL")


#设置STL图形的mapper和actor
mapperSTL = vtk.vtkPolyDataMapper()
mapperSTL.SetInputConnection(stlReader.GetOutputPort())   #设置mapper数据源

actorSTL = vtk.vtkActor()
actorSTL.SetMapper(mapperSTL)
actorSTL.GetProperty().SetColor(0.7, 0.7, 0.7)   # 0.7-白色

#设置图形轮廓的mapper和actor
outlineFilter = vtk.vtkOutlineFilter()
outlineFilter.SetInputConnection(stlReader.GetOutputPort())

mapperOutline = vtk.vtkPolyDataMapper()
mapperOutline.SetInputConnection(outlineFilter.GetOutputPort())

actorOutline = vtk.vtkActor()
actorOutline.SetMapper(mapperOutline)
actorOutline.GetProperty().SetColor(0.1, 0.1, 0.1)

#显示
renderer = vtk.vtkRenderer()   #渲染器
renderer.AddActor(actorSTL)
renderer.AddActor(actorOutline)
renderer.SetBackground(0.1, 0.2, 0.4)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
window.SetSize(900, 600)
window.Render()

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())   #设置交互方式
interactor.Initialize()  
interactor.Start()