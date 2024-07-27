import math
from screen import Screen
import consts

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y + other.y)
    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)
    def __floordiv__(self, other):
        return Vector2(self.x // other.x, self.y // other.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"

def edgeFunction(a: Vector2, b: Vector2, p: Vector2):
    return (a.y - b.y) * (p.x - a.x) - (b.x - a.x) * (a.y - p.y);

def crossProduct(a: Vector2, b: Vector2):
    return a.x * b.y - a.y * b.x;

def sortClockwise(a: Vector2, b: Vector2, c: Vector2):
    if (crossProduct(b - a, c - a) < 0):
        b, c = c, b

class Triangle:
    def __init__(self, a: Vector2, b: Vector2, c: Vector2):
        self.a, self.b, self.c = a, b, c
    
    def sortPoints(self):
        sortClockwise(self.a, self.b, self.c)
    
    def isInside(self, p: Vector2) -> bool:
        self.sortPoints()
        return edgeFunction(self.a, self.b, p) <= 0 and edgeFunction(self.b, self.c, p) <= 0 and edgeFunction(self.c, self.a, p) <= 0

    def render(self, screen: Screen):
        #define bounding box
        start = Vector2(min(self.a.x, self.b.x, self.c.x), min(self.a.y, self.b.y, self.c.y))
        end = Vector2(max(self.a.x, self.b.x, self.c.x), max(self.a.y, self.b.y, self.c.y))

        center = Vector2(consts.PIXEL_WIDTH // 2, consts.PIXEL_HEIGHT // 2)

        for x in range(math.floor(start.x), math.floor(end.x + 1)):
            for y in range(math.floor(start.y), math.floor(end.y + 1)):
                if self.isInside(Vector2(x, y)):
                    screen.setPixel(center.x + x, center.y + y, 1.0)
# class Rect:

# class Circle: