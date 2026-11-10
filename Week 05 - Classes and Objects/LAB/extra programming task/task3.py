class Rectangle:
    def __init__(self, width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

Rectangles = [
    Rectangle(3, 4),
    Rectangle(5, 5),
    Rectangle(2, 10),
    Rectangle(6, 3),
]

for i, rect in enumerate(Rectangles, start=1):
    print(f"Rectangle {i} ({rect.width}x{rect.height}): "
          f"Area = {rect.area()}, Perimeter = {rect.perimeter()}")

largest = max(Rectangles, key=lambda r: r.area())
print(f"\nLargest area: {largest.width}x{largest.height} with area {largest.area()}")
