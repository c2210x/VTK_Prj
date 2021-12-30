import math
import CmGeomBase
import CmLine
import CmRay

def IsNearZero(x):
    return True if math.fabs(x) < CmGeomBase.epsilon else False

def Distance(obj1, obj2):
    if isinstance(obj1, CmGeomBase.Point3D) and isinstance(obj2, CmLine.Line):
        P, Q, V = obj2.P, obj1, obj2.V
        t = P.PointTo(Q).DotProduct(V)
        R = P + V.Amplified(t)
        return Q.Distance(R)
    elif isinstance(obj1, CmGeomBase.Point3D) and isinstance(obj2, CmRay.Ray):
        P, Q, V = obj2.P, obj1, obj2.V


print("")