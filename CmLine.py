# from CmGeomBase import *

import CmGeomBase

class Line:
    def __init__(self, P, V) -> None:
        self.P = CmGeomBase.Point3D.Clone(P)
        self.V = CmGeomBase.Vector3D.Clone(V).Normalized()
    # def __init__(self, P, V) -> None:
    #     self.P = P
    #     self.V = V
    def __str__(self) -> str:
        return "Line\nPoint %s\nVector %s\n" %(str(self.P), str(self.V))