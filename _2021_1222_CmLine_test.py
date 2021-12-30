import CmGeomBase
import CmLine

p = CmGeomBase.Point3D(1, 2, 3)
v = CmGeomBase.Vector3D(4, 5, 6)
line = CmLine.Line(p, v)
print(line)
p.x = 0   #如果init方法不是clone，那么点x会改变。
print(line)