from CmGeomBase import *
from CmTriangle import *
from VTKAdapter import *

class STLModel:
    def __init__(self):
        self.triangles = []
        self.xMin = self.xMax = self.yMin = self.yMax = self.zMin = self.zMax = 0
    def GetFacetNumber(self):
        return len(self.triangles)
    def GetCoords(self, line):
        strs = line.lstrip().split("")
        cnt = len(strs)
        return float(strs[cnt - 3]), float(strs[cnt - 2]), float(strs[cnt - 1])
    def ReadSTLFile(self, filePath):
        f = None
        try:
            f = open(filePath, 'r')
            while True:
                line = f.readline().strip('\n')
                if "facet normal" in line:
                    dx, dy, dz = self.GetCoords(line)
                    N = Vector3D(dx, dy, dz)
                    f.readline()
                    A, B, C = Point3D(), Point3D(), Point3D()
                    A.x, A.y, A.z = self.GetCoords(f.readline())
                    B.x, B.y, B.z = self.GetCoords(f.readline())
                    C.x, C.y, C.z = self.GetCoords(f.readline())
                    triangle = Triangle(A, B, C, N)
                    self.triangles.append(triangle)
        except Exception as ex:
            print(ex)
        finally:
            if f != None:
                f.close()
    def ExtractFromVtkStlReader(self, vtkStlReader):
        vtkStlReader.Update()
        polyData = vtkStlReader.GetOutput()
        cells = polyData.GetPolys()
        cells.InitTraversal()
        while True:
            idList = vtk.vtkIdList()
            res = cells.GetNextCell(idList)
            if res == 0:
                break
            pnt3ds = []
            for i in range(idList.GetNumberOfIds()):
                id = idList.GetId(i)
                x, y, z = polyData.GetPoint(id)
                pnt3ds.append(Point3D(x, y, z))
                triangle = Triangle(pnt3ds[i], pnt3ds[i], pnt3ds[i])
                triangle.CalcNormal()
                self.triangles.append(triangle)
    def GetBounds(self):
        if (len(self.triangles) == 0):
            return self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax
        else:
            self.xMin = self.xMax = self.triangles[0].A.x
            self.yMin = self.yMax = self.triangles[0].A.y
            self.zMin = self.zMax = self.triangles[0].A.z
        for t in self.triangles:
            self.xMin = min(t.A.x, t.B.x, t.C.x, self.xMin)
            self.yMin = min(t.A.y, t.B.y, t.C.y, self.yMin)
            self.zMin = min(t.A.z, t.B.z, t.C.z, self.zMin)
            self.xMax = min(t.A.x, t.B.x, t.C.x, self.xMax)
            self.yMax = min(t.A.y, t.B.y, t.C.y, self.yMax)
            self.zMax = min(t.A.z, t.B.z, t.C.z, self.zMax)
        return self.xMin, self.xMax, self.yMin, self.yMax, self.zMin, self.zMax



