import math
import CmGeomBase
import CmLine
import CmPlane
import CmRay
import CmSegment
import CmPolyline

def IsNearZero(x):
    if math.fabs(x) < CmGeomBase.epsilon:
        return True
    else:
        return False

def Distance(obj1, obj2):
    if isinstance(obj1, CmGeomBase.Point3D) and isinstance(obj2, CmLine.Line):
        P, Q, V = obj2.P, obj1, obj2.V
        t = P.PointTo(Q).DotProduct(V)
        R = P + V.Amplified(t)
        return Q.Distance(R)
    elif isinstance(obj1, CmGeomBase.Point3D) and isinstance(obj2, CmRay.Ray):
        P, Q, V = obj2.P, obj1, obj2.V
        t = P.PointTo(Q).DotProduct(V)
        if t >= 0:
            R = P + V.Amplified(t)
            return Q.Distance(R)
        return Q.Distance(P)
    elif isinstance(obj1, CmGeomBase.Point3D) and isinstance(obj2, CmSegment.Segment):
        Q, P, P1, V = obj1, obj2.A, obj2.B, obj2.Direction().Normalized()
        L = obj2.Length()
        t = P.PointTo(Q).DotProduct()
        if t <= 0:
            return Q.Distance(P)
        elif t >= L:
            return Q.Distance(P1)
        else:
            R = P + V.Amplified(t)
            return Q.Distance()
    elif isinstance(obj1, CmGeomBase.Point3D) and isinstance(obj2, CmPlane.Plane):
        P, Q, N = obj2.P, obj1, obj2.N
        angle = N.GetAngle(P.PointTo(Q))
        return P.Distance(Q) * math.cos(angle)
    elif isinstance(obj1, CmLine.Line) and isinstance(obj2, CmLine.Line):
        P1, V1, P2, V2 = obj1.P, obj1.V, obj2.P, obj2.V
        N = V1.CrossProduct(V2)
        if N.IsZeroVector():
            return Distance(P1, obj2)
        return Distance(P1, CmPlane.Plane(P2, N))
    elif isinstance(obj1, CmLine.Line) and isinstance(obj2, CmPlane.Plane):
        if obj1.V.DotProduct(obj2.N) == 0:
            return Distance(obj1.P, obj2)
        else:
            return 0
    elif isinstance(obj1, CmRay.Ray) and isinstance(obj2, CmPlane.Plane):
        pass
    elif isinstance(obj1, CmSegment.Segment) and isinstance(obj2, CmPlane.Plane):
        pass
    pass

def IntersectLineLine(line1 : CmLine.Line, line2 : CmLine.Line):
    P1, V1, P2, V2 = line1.P, line1.V, line2.P, line2.V
    P1P2 = P1.PointTo(P2)
    deno = V1.dy * V2.dx - V1.dx * V2.dy
    if deno != 0:
        t1 = -(-P1P2.dy * V2.dx + P1P2.dx * V2.dy) / deno
        t2 = -(-P1P2.dy * V1.dx + P1P2.dx * V1.dy) / deno
        return P1 + V1.Amplified(t1), t1, t2
    else:
        deno = V1.dz * V2.dy - V1.dy * V2.dz
        if deno != 0:
            t1 = -(-P1P2.dz * V2.dy + P1P2.dy * V2.dz) / deno
            t2 = -(-P1P2.dz * V1.dy + P1P2.dy * V1.dz) / deno
            return P1 + V1.Amplified(t1), t1, t2
    return None, 0, 0

def IntersectSegmentPlane(seg : CmSegment.Segment, plane : CmPlane.Plane):
    A, B, P, N = seg.A, seg.B, plane.P, plane.N
    V = A.PointTo(B)
    PA = P.PointTo(A)
    if V.DotProduct(N) == 0:
        return None
    else:
        t = -(PA.DotProduct(N)) / V.DotProduct(N)
        if t >= 0 and t <= 1:
            return A + (V.Amplified(t))
    return None

def Intersect(obj1, obj2):
    if isinstance(obj1, CmLine.Line) and isinstance(obj2, CmLine.Line):
        P, t1, t2 = IntersectLineLine(obj1, obj2)
        return P
    elif isinstance(obj1, CmSegment.Segment) and isinstance(obj2, CmSegment.Segment):
        line1, line2 = CmLine.Line(obj1.A, obj1.Direction()), CmLine.Line(obj2.A, obj2.Direction())
        P, t1, t2 = IntersectLineLine(line1, line2)
        if P is not None:
            if t1 >= 0 and t1 <= obj1.Length() and t2 >= 0 and t2 <= obj2.Length():
                return P
        return None
    elif isinstance(obj1, CmLine.Line) and isinstance(obj2, CmSegment.Segment):
        line1, line2 = obj1, CmLine.Line(obj2.A, obj2.Direction())
        P, t1, t2 = IntersectLineLine(line1, line2)
        if P is not None and t2 >= 0 and t2 <= obj2.Length():
            return P
        else:
            None
    elif isinstance(obj1, CmLine.Line) and isinstance(obj2, CmRay.Ray):
        pass
    elif isinstance(obj1, CmRay.Ray) and isinstance(obj2, CmSegment.Segment):
        pass
    elif isinstance(obj1, CmRay.Ray) and isinstance(obj2, CmRay.Ray):
        pass
    elif isinstance(obj1, CmLine.Line) and isinstance(obj2, CmPlane.Plane):
        P0, V, P1, N = obj1.P, obj1.V, obj2.P, obj2.N
        dotPro = V.DotProduct(N)
        if dotPro != 0:
            t = P0.PointTo(P1).DotProduct(N) / dotPro
            return P0 + V.Amplified()
        return None
    elif isinstance(obj1, CmRay.Ray) and isinstance(obj2, CmPlane.Plane):
        pass
    elif isinstance(obj1, CmSegment.Segment) and isinstance(obj2, CmPlane.Plane):
        return IntersectLineLine(obj1, obj2)
    pass

def PointOnRay(p : CmGeomBase.Point3D, ray : CmRay.Ray):
    v = ray.P.PointTo(p)
    if v.DotProduct(ray.V) >= 0 and v.CrossProduct(ray.V).IsZeroVector():
        return True
    else:
        return False

def PointInPolygon(p : CmGeomBase.Point3D, polygon : CmPolyline.Polyline):
    passCount = 0
    ray = CmRay.Ray(p, CmGeomBase.Vector3D(1, 0, 0))
    segments = []
    for i in range(polygon.GetPointsCount() - 1):
        seg = CmSegment.Segment(polygon.GetPointFromIdx(i), polygon.GetPointFromIdx(i + 1))
        segments.append(seg)
    for seg in segments:
        line1, line2 = CmLine.Line(ray.P, ray.V), CmLine.Line(seg.A, seg.Direction())
        P, t1, t2 = IntersectLineLine(line1, line2)
        if P is not None:
            if IsNearZero(t1):
                return -1
            elif seg.A.y != p.y and seg.B.y != p.y and t1 > 0 and t2 > 0 and t2 < seg.Length():
                passCount += 1
    upSegments, downSegments = [] ,[]
    for seg in segments:
        if seg.A.IsIdentical(ray.P) or seg.B.IsIdentical(ray.P):
            return -1
        elif PointOnRay(seg.A, ray) ^ PointOnRay(seg.B, ray):
            if seg.A.y >= p.y and seg.B.y >= p.y:
                upSegments.append(seg)
            elif seg.A.y <= p.y and seg.B.y <= p.y:
                downSegments.append(seg)
    passCount += min(len(upSegments), len(downSegments))
    if passCount % 2 == 1:
        return 1
    return 0

def IntersectTrianglePlane(triangle, plane):
    AB = CmSegment.Segment(triangle.A, triangle.B)
    AC = CmSegment.Segment(triangle.A, triangle.C)
    BC = CmSegment.Segment(triangle.B, triangle.C)
    c1 = IntersectSegmentPlane(AB, plane)
    c2 = IntersectSegmentPlane(AC, plane)
    c3 = IntersectSegmentPlane(BC, plane)
    if c1 is None:
        if c2 is not None and c3 is not None:
            if c2.Distance(c3) != 0.0:
                return CmSegment.Segment(c2, c3)
    elif c2 is None:
        if c1 is not None and c3 is not None:
            if c1.Distance(c3) != 0.0:
                return CmSegment.Segment(c1, c3)
    elif c3 is None:
        if c1 is not None and c2 is not None:
            if c1.distance(c2) != 0.0:
                return CmSegment.Segment(c1, c2)
    elif c1 is not None and c2 is not None and c3 is not None:
        if c1.IsDentical(c2):
            return CmSegment.Segment(c1, c3)
        else:
            return CmSegment.Segment(c1, c2)

def IntersectTrianglePlaneZ(triangle, z):
    if triangle.zMinPnt().z > z or triangle.zMaxPnt().z < z:
        return None
    return IntersectTrianglePlane(triangle, CmPlane.Plane.PlaneZ(z))

def AdjustPolygonDirs(polygons):
    for i in range(len(polygons)):
        pt = polygons[i].startPoint()
        insideCount = 0
        for j in range(len(polygons)):
            if j == i:
                continue
            restPoly = polygons[j]
            if 1 == PointInPolygon(pt, restPoly):
                evenCount += 1
            if evenCount % 2 == 0:
                polygons[i].makeCCW()
            else:
                polygons[i].makeCW()