import CmGeomBase
import CmSegment

class Polyline:
    def __init__(self) -> None:
        self.points = []
    def __str__(self) -> str:
        pass
    def Clone(self):
        poly = Polyline()
        for pt in self.points:
            poly.AddPoints(pt.Clone())
        return poly   #存疑
    def GetPointsCount(self):
        return len(self.points)
    def AddPoint(self, pt):
        self.points.append(pt)
    def AddTuple(self, tuple):
        self.points.append(CmGeomBase.Point3D(tuple[0], tuple[1], tuple[2]))
    def RevAddPoint(self, pt):
        self.points.insert(0, pt)
    def RemovePoint(self, index):
        return self.points.pop(index)
    def GetPointFromIdx(self, index):
        return self.points[index]
    def GetStartPoint(self):
        return self.points[0]
    def GetEndPoint(self):
        return self.points[-1]
    def IsPolylineClosed(self):
        if self.GetPointsCount() <= 2:
            return False
        return self.GetStartPoint().IsCoincide(self.GetEndPoint())
    def Reverse(self):
        sz = self.GetPointsCount()
        for i in range(int(sz / 2)):
            sz[i], sz[sz - 1 - i] = sz[sz - 1 - i], sz[i]
    def GetXYArea(self):
        area = 0.0
        for i in range(self.GetPointsCount() - 1):
            area += 0.5 * (self.points[i].x * self.points[i + 1].y - self.points[i + 1].x * self.points[i].x)
        return area
    def MakeXYCCW(self):
        if self.GetXYArea() < 0:
            self.Reverse()
    def MakeXYCW(self):
        if self.GetXYArea() > 0:
            self.Reverse()
    def IsXYCCW(self):
        return True if self.GetXYArea() > 0 else False
    def Translate(self, vec):
        for i in range(self.GetPointsCount()):
            self.points[i].Translate(vec)   #不太懂
    def AppendSegment(self, seg : CmSegment):
        if self.GetPointsCount() == 0:
            self.points.append(seg.A)
            self.points.append(seg.B)
        else:
            if seg.A.IsCoincide(self.GetEndPoint()):
                self.AddPoint(seg.B)
            elif seg.B.IsCoincide(self.GetEndPoint()):
                self.AddPoint(seg.A)
            elif seg.A.IsCoincide(self.GetStartPoint()):
                self.RevAddPoint(seg.B)
            elif seg.B.IsCoincide(self.GetStartPoint()):
                self.RevAddPoint(seg.A)
            else:
                return False
        return True

# 以下为全局函数
def WritePolylineToFile(path, polyLine : Polyline):
    file = None
    try:
        file = open(path, 'w')
        file.write("Points count is: %s\n" %polyLine.GetPointsCount())
        for pt in polyLine.points:
            txt = "(%s, %s, %s)\n" %(pt.x, pt.y, pt.z)
            file.write(txt)
    except Exception as e:
        print(e)
    finally:
        if file != None:
            file.close()

def ReadPolylineFromFile(path):
    file = None
    try:
        file = open(path, 'r')
        poly = Polyline()
        number = int(file.readline())
        for i in range(number):
            txt = file.readline()
            txts = txt.split(',')
            x, y, z = float(txts[0]), float(txts[1]), float(txts[2])
            poly.AddPoint(CmGeomBase.Point3D(x, y, z))
        return poly
    except Exception as e:
        print(e)
    finally:
        if file != None:
            file.close()
    