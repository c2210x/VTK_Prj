import CmGeomBase

class Segment:
    def __init__(self, A, B) -> None:
        self.A, self.B = CmGeomBase.Point3D.Clone(A), CmGeomBase.Point3D.Clone(B)
    def __str__(self) -> str:
        return "Segment\nA %s\nB %s\n" %(str(self.A), str(self.B))
    def Length(self):
        return CmGeomBase.Point3D.Distance(self.A, self.B)
    def Direction(self):
        return self.A.PointTo(self.B)
    def Swap(self):
        self.A, self.B = self.B, self.A