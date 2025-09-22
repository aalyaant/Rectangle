#Alyce Gaines
#CSI261
#Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def draw(self):
        drawing = '* ' * self.width + '\n'
        for _ in range(self.height - 2):
            drawing += '* ' + '  ' * (self.width - 2) + '* \n'
        drawing += '* ' * self.width + '\n'
        return drawing

    def __str__(self):
        return f"Height: {self.height}\nWidth: {self.width}\nPerimeter: {self.perimeter()}\nArea: {self.area()}"


def main():
    continue_drawing = 'y'
    while continue_drawing.lower() == 'y':
        height = int(input("rectangle height: "))
        width = int(input("rectangle width: "))
        rect = Rectangle(height, width)
        print(rect)
        print(rect.draw())
        continue_drawing = input("continue? (y/n): ")

if __name__ == "__main__":
    main()