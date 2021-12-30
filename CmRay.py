import CmGeomBase

class Ray:
    def __init__(self, pt, vec) -> None:
        self.pt = CmGeomBase.Point3D.Clone(pt)
        self.vec = CmGeomBase.Vector3D.Clone(vec).Normalized()
    def __str__(self) -> str:
        return "Ray\nPoint %s\nVector %s\n" %(str(self.pt), str(self.vec))