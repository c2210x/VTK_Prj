import CmGeomBase
import CmSegment

A = CmGeomBase.Point3D(0, 0, 0)
B = CmGeomBase.Point3D(0, 0, 2)
line = CmSegment.Segment(A, B)
dis = CmSegment.Segment.Length(line)
print(line)
print(dis)