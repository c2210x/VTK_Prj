from CmGeomBase import *

class Triangle:
    def __init__(self, A : Point3D, B : Point3D, C : Point3D, N = Vector3D(0, 0, 0)):
        self.A, self.B, self.C, self.N = A.Clone(), B.Clone(), C.Clone, N.Clone()
        self.zs = []
    def __str__(self):
        pass
    def ZMinPnt(self):
        pass
    def ZMaxPnt(self):
        pass
    def CalcNormal(self):
        pass