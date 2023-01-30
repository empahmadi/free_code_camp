class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def get_picture(self):
        result = ''
        if self.height < 51 and self.width < 51:
            for i in range(self.height):
                result += '{character:*<{width}}\n'.format(character='*', width=self.width)
        else:
            result += 'Too big for picture.'
        return result

    def get_amount_inside(self, shape):
        h = int(self.width/shape.width)
        v = int(self.height/shape.height)
        return v * h

    def __str__(self):
        return 'Rectangle(width={0}, height={1})'.format(self.width, self.height)


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def get_area(self):
        return self.side ** 2

    def get_diagonal(self):
        return self.side * (2 ** 0.5)

    def get_perimeter(self):
        return 4 * self.side

    def get_picture(self):
        return super().get_picture()

    def get_amount_inside(self, shape):
        return super().get_amount_inside(shape)

    def __str__(self):
        return 'Square(side={0})'.format(self.side)


def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))


if __name__ == '__main__':
    main()
