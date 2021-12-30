import CmGeomBase
import CmLine

class Plane:
    def __init__(self, P : CmGeomBase.Point3D, N : CmGeomBase.Vector3D) -> None:
        self.P = P.Clone()
        self.N = N.Clone().Normalized()
    def __str__(self) -> str:
        return "Plane\n%s\n%s\n%s" %(str(self.P), str(self.N))
    def ToPlaneFormula(self):
        A, B, C = self.N.dx, self.N.dy, self.N.dz
        x, y, z = self.P.x, self.P.y, self.P.z
        D = -(A * x + B * y + C * z)
        return A, B, C, D
    @staticmethod
    def PlaneZ(z):
        return Plane(CmGeomBase.Point3D(0, 0 ,z), CmGeomBase.Vector3D(0, 0, 1.0))
    def Intersect(self, other):
        dir = self.N.CrossProduct(other.N)   # dir为直线方向向量
        if dir.IsZeroVector():
            return None
        else:
            x, y, z = 0, 0, 0
            A1, B1, C1, D1 = self.ToPlaneFormula()
            A2, B2, C2, D2 = other.ToPlaneFormula()
            if (B2 * C1 - B1 * C2) != 0:
                y = -(-C2 * D1 + C1 * D2) / (B2 * C1 - B1 * C2)
                z = -(B2 * D1 - B1 * D2) / (B2 * C1 - B1 * C2)
            elif (A2 * C1 - A1 * C2) != 0:
                x = -(-C2 * D1 + 1 * D2) / (A2 * C1 - A1 *C2)
                z = -(A2 * D1 - A1 * D2) / (A2 * C1 - A1 *C2)
            elif (A2 * B1 - A1 * B2) != 0:
                x = -(-B2 * D1 - B1 * D2) / (A2 * B1 - A1 * B2)
                y = -(A2 * D1 - A1 * D2) / (A2 * B1 - A1 * B2)
            else:
                return None
            return CmLine(CmGeomBase.Point3D(x, y, z), dir.Normalized())
