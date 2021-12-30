import math

epsilon = 1e-7
epsilonSquare = epsilon * epsilon


class Point3D:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0, w = 1.0) -> None:
        self.x, self.y, self.z, self.w = x, y, z, w
    def __str__(self) -> str:
        return "Point3D: %s，%s，%s" %(self.x, self.y, self.z)
    def __add__(self, vec):
        return self.Translated(vec)
    def __sub__(self, other):
        pass
    def __mul__(self, matrix):
        return self.Multiplied(matrix)
    def Clone(self):
        return Point3D(self.x, self.y, self.z, self.w)
    def PointTo(self, other):
        return Vector3D(other.x - self.x, other.y - self.y, other.z - self.z)
    def Translate(self, vec):
        self.x, self.y, self.z = self.x + vec.dx, self.y + vec.dy, self.z + vec.dz
    def Translated(self, vec):
        return Point3D(self.x + vec.dx, self.y + vec.dy, self.z + vec.dz)
    def Multiplied(self, matrix):
        x = self.x * matrix.a[0][0] + self.y * matrix.a[1][0] + self.z * matrix.a[2][0] + self.w * matrix.a[3][0]
        y = self.x * matrix.a[0][1] + self.y * matrix.a[1][1] + self.z * matrix.a[2][1] + self.w * matrix.a[3][1]
        z = self.x * matrix.a[0][2] + self.y * matrix.a[1][2] + self.z * matrix.a[2][2] + self.w * matrix.a[3][2]
        return Point3D(x, y, z)
    def Distance(self, other):
        return self.PointTo(other).Length()
    def DistanceSquare(self, other):
        return self.PointTo(other).LengthSquare()
    def Middle(self, other):
        return Point3D((self.x + other.x) / 2, (self.y + other.y) / 2, (self.z + other.z) / 2)
    def IsCoincide(self, other, dis = epsilonSquare):
        pass
    def IsDentical(self, other):
        return True if self.x == other.x and self.y == other.y and self.z == other.z else False
    
class Vector3D:
    def __init__(self, dx = 0.0, dy = 0.0, dz = 0.0, dw = 0.0) -> None:
        self.dx, self.dy, self.dz, self.dw = dx, dy, dz, dw
    def __str__(self) -> str:
        return "Vector3D: %s, %s, %s" %(self.dx, self.dy, self.dz)
    def __add__(self, other):
        return Vector3D(self.dx + other.dx, self.dy + other.dy, self.dz + other.dz)
    def __sub__(self, other):
        return self + other.Reversed()
    def __mul__(self, other):
        return self.Multiplied(other)
    def Clone(self):
        return Vector3D(self.dx, self.dy, self.dz, self.dw)
    def Reverse(self):
        self.dx, self.dy, self.dz = -self.dx, -self.dy, -self.dz
    def Reversed(self):
        return Vector3D(-self.dx, -self.dy, -self.dz)
    def DotProduct(self, vec):
        return self.dx * vec.dx + self.dy * vec.dy + self.dz * vec.dz
    def CrossProduct(self, vec):
        dx = self.dy * vec.dz - self.dz * vec.dy
        dy = self.dz * vec.dx - self.dx * vec.dz
        dz = self.dx * vec.dy - self.dy * vec.dx
        return Vector3D(dx, dy, dz)
    def Amplify(self, f):
        self.dx, self.dy, self.dz = self.dx * f, self.dy * f, self.dz * f
    def Amplified(self, f):
        return Vector3D(self.dx * f, self.dy * f, self.dz * f)
    def LengthSquare(self):
        return self.dx ** 2 + self.dy ** 2 + self.dz ** 2
    def Length(self):
        return math.sqrt(self.LengthSquare())
    def Normalize(self):
        len = self.Length()
        self.dx, self.dy, self.dz = self.dx / len, self.dy / len, self.dz / len
    def Normalized(self):
        len = self.Length()
        return Vector3D(self.dx / len, self.dy / len, self.dz / len)
    def IsZeroVector(self):
        return self.LengthSquare == 0.0
    def Multiplied(self, matrix):
        dx = self.dx * matrix.a[0][0] + self.dy * matrix.a[1][0] + self.dz * matrix.a[2][0] + self.dw * matrix.a[3][0]
        dy = self.dx * matrix.a[0][1] + self.dy * matrix.a[1][1] + self.dz * matrix.a[2][1] + self.dw * matrix.a[3][1]
        dz = self.dx * matrix.a[0][2] + self.dy * matrix.a[1][2] + self.dz * matrix.a[2][2] + self.dw * matrix.a[3][2]
        return Vector3D(dx, dy, dz)
    def IsParallel(self, other):
        return self.CrossProduct(other).IsZeroVector()
    def GetAngle(self, vec):
        v1, v2 = self.Normalized(), vec.Normalized()
        dotPro = v1.DotProduct(v2)
        if dotPro > 1:
            dotPro = 1
        elif dotPro < -1:
            dotPro = -1
        return math.acos(dotPro)
    def GetOrthoVector2D(self):
        if self.dx == 0:
            return Vector3D(1, 0, 0).Normalized()
        else:
            return Vector3D(-self.dy / self.dx, 1, 0).Normalized()
    def GetAngle2D(self):
        rad = self.GetAngle(Vector3D(1, 0, 0))
        if self.dy < 0:
            rad = math.pi * 2.0 - rad
        return rad
    

class Matrix3D:
    def __init__(self) -> None:
        self.a = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]
    def __str__(self) -> str:
        return "Matrix3D: \n%s\n%s\n%s\n%s" %(self.a[0], self.a[1], self.a[2], self.a[3])
    def __mul__(self, other):
        return self.Multiplied(other)
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def MakeIdentical(self):
        self.a = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]]
    def Multiplied(self, other):
        m = Matrix3D()
        for i in range(4):
            for j in range(4):
                m.a[i][j] = self.a[i][0] * other.a[0][j] + \
                            self.a[i][1] * other.a[1][j] + \
                            self.a[i][2] * other.a[2][j] + \
                            self.a[i][3] * other.a[3][j]
        return m
    def GetDeterminant(self):
        pass
    def GetReverseMatrix(self):
        pass
    @ staticmethod
    def CreateTranlsateMatrix(dx, dy, dz):
        m = Matrix3D()
        m.a[3][0], m.a[3][1], m.a[3][2] = dx, dy, dz
        return m
    @ staticmethod
    def CreateScalMatrix(sx, sy, sz):
        m = Matrix3D()
        m.a[0][0], m.a[1][1], m.a[2][2] = sx, sy, sz
        return m
    @ staticmethod
    def CreateRotateMatrix(axis, angle):
        m = Matrix3D()
        sin, cos = math.sin(angle), math.cos(angle)
        if axis == 'X' or axis == 'x':
            m.a[1][1], m.a[1][2], m.a[2][1], m.a[2][2] = cos, sin, -sin, cos
        elif axis == 'Y' or axis == 'y':
            m.a[0][0], m.a[0][2], m.a[2][0], m.a[2][2] = cos, -sin, sin, cos
        elif axis == 'Z' or axis == 'z':
            m.a[0][0], m.a[0][1], m.a[1][0], m.a[1][1] = cos, sin, -sin, cos
        return m
    @ staticmethod
    def CreateMirrorMatrix(point, normal):
        pass

