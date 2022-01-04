import CmGeomBase

class Ray:
    def __init__(self, P, V) -> None:
        self.P = CmGeomBase.Point3D.Clone(P)
        self.V = CmGeomBase.Vector3D.Clone(V).Normalized()
    def __str__(self) -> str:
        return "Ray\nPoint %s\nVector %s\n" %(str(self.P), str(self.V))