from VTKAdapter import *

vtkAdapter = VTKAdapter(bgClr = (0.95, 0.95, 0.95))
vtkAdapter.DrawAxes()
actor1 = vtkAdapter.DrawSTLModel("D:\\_Design Software\\Python\\Download_Misc\\STL\\3D.STL")
actor2 = vtkAdapter.DrawSTLModel("D:\\_Design Software\\Python\\Download_Misc\\STL\\3D.STL")
x, y, z = actor2.GetPosition()
x += 125.0
actor2.SetPosition(x, y, z)
sx, sy, sz = actor2.GetScale()
sx, sy, sz = sx / 2.0, sy / 2.0, sz / 2.0
actor2.SetScale(sx, sy, sz)
vtkAdapter.Display()