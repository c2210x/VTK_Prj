from CmStlModel import *
from CmStlLayer import *
from VTKAdapter import *
import vtkmodules.all as vtk

def IntersectSTL_brutal(stlModel : STLModel, layerThick):
    layers = []
    xMin, xMax, yMin, yMax, zMin, zMax = stlModel.GetBounds()
    z = zMin + layerThick
    while z < zMax:
        layer = Layer(z)
        for tri in stlModel.triangles:
            seg = IntersectTrianglePlaneZ(tri, z)
            if seg is not None:
                layer.segments.append(seg)
        layers.append(layer)
        z += layerThick
    return layers

if __name__ == '__main__':
    vtkAdapter = VTKAdapter()
    vtkStlReader = vtk.vtkSTLReader()
    vtkStlReader.SetFileName("D:\\_Design Software\\Python\\Download_Misc\\STL\\3D.STL")
    vtkAdapter.DrawPdSrc(vtkStlReader).GetProperty().SetOpacity(0.5)
    stlModel = STLModel()
    stlModel.ExtractFromVtkStlReader(vtkStlReader)
    layers = IntersectSTL_brutal(stlModel, 10.0)
    for layer in layers:
        for seg in layer.segments:
            segActor = vtkAdapter.DrawSegment(seg)
            segActor.GetProperty().SetLineWidth(2)
    vtkAdapter.Display()

