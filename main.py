import screen
from geometry import Triangle
from geometry import Vector2
import geometry
from time import sleep

def main():
    foo = screen.Screen()
    
    # print(geometry.edgeFunction(Vector2(0, 0), Vector2(100, 0), Vector2(0, 100)))

    triangle = Triangle(Vector2(-100, -100), Vector2(-100, 100), Vector2(100, 100))
    triangle.render(foo)

    foo.update()
    foo.display()

if __name__ == "__main__":
    main()