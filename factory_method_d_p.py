from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Trangle(Shape):
    def draw(self):
        print("Drawing Trangle")


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


def draw_shape(shape):
    match shape.lower():
        case "circle":
            return Circle()
        case "trangle":
            return Trangle()
        case _:
            raise ValueError("Unknown Shape Type")


if __name__ == "__main__":
    input_shape = input("Enter a shape to draw")
    object_ = draw_shape(input_shape)
    object_.draw()

