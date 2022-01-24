from VTKAdapter import *

if __name__ == '__main__':
    vtkAdapter = VTKAdapter()
    vtkAdapter.SetBackGroundColor(0.95, 0.95, 0.95)
    vtkAdapter.DrawAxes()
    vtkAdapter.DrawPoint(CmGeomBase.Point3D(10, 10, 10)).GetProperty().SetColor(1, 0, 0)
    vtkAdapter.DrawPoint(CmGeomBase.Point3D(50, 50, 50)).GetProperty().SetColor(1, 0, 0)
    polyline = CmPolyline.Polyline()
    polyline.AddPoint(CmGeomBase.Point3D(1, 1, 1))
    polyline.AddPoint(CmGeomBase.Point3D(50, 2, 10))
    polyline.AddPoint(CmGeomBase.Point3D(20, 10, 30))
    polyline.AddPoint(CmGeomBase.Point3D(50, 80, 55))
    polylineActor = vtkAdapter.DrawPolyline(polyline)
    polylineActor.GetProperty().SetColor(0.1, 0.7, 0.7)
    polylineActor.GetProperty().SetLineWidth(2)
    stlActor = vtkAdapter.DrawSTLModel("D:\\_Design Software\\Python\\Download_Misc\\STL\\3D.STL")
    stlActor.SetPosition(0, 150, 150)
    vtkAdapter.Display()

