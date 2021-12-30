import CmGeomBase

p1 = CmGeomBase.Point3D(1, 1, 1)
p2 = CmGeomBase.Point3D(2, 3, 4)
# v = p1.PointTo(p2)
# print(v)

v = CmGeomBase.Vector3D(1, 1, 1)
p1.Translate(v)
