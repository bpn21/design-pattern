# Without Design Pattern

class Car:
    def __init__(self, engine, wheels, color, interior):
        self.engine = engine
        self.wheels = wheels
        self.color = color
        self.interior = interior

    def __str__(self):
        return f"Car with {self.engine}, {self.wheels} wheels, color {self.color}, and {self.interior} interior"


# Client Code: Creating a complex car object manually
if __name__ == "__main__":
    # Manually specifying all the parts
    car1 = Car("V8 Engine", "4 sporty wheels", "Red", "Leather seats")
    print("Car 1:", car1)

    car2 = Car("V6 Engine", "4 rugged wheels", "Blue", "Fabric seats")
    print("Car 2:", car2)




#Using Builder Design Pattern
# from abc import ABC, abstractmethod


# Product: Car
class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None
        self.interior = None

    def __str__(self):
        return f"Car with {self.engine}, {self.wheels} wheels, color {self.color}, and {self.interior} interior"


# Abstract Builder
class CarBuilder(ABC):
    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_wheels(self):
        pass

    @abstractmethod
    def build_color(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    @abstractmethod
    def get_car(self):
        pass


# Concrete Builder for SportsCar
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "V8 Engine"

    def build_wheels(self):
        self.car.wheels = "4 sporty wheels"

    def build_color(self):
        self.car.color = "Red"

    def build_interior(self):
        self.car.interior = "Leather seats"

    def get_car(self):
        return self.car


# Concrete Builder for SUV
class SUVCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "V6 Engine"

    def build_wheels(self):
        self.car.wheels = "4 rugged wheels"

    def build_color(self):
        self.car.color = "Blue"

    def build_interior(self):
        self.car.interior = "Fabric seats"

    def get_car(self):
        return self.car


# Director: Orchestrates the construction of a car
class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        self.builder.build_engine()
        self.builder.build_wheels()
        self.builder.build_color()
        self.builder.build_interior()

    def get_car(self):
        return self.builder.get_car()


# Client Code
if __name__ == "__main__":
    # Building a Sports Car using the SportsCarBuilder
    sports_car_builder = SportsCarBuilder()
    director = CarDirector(sports_car_builder)
    director.construct_car()
    sports_car = director.get_car()
    print("Sports Car:", sports_car)

    print()

    # Building an SUV Car using the SUVCarBuilder
    suv_car_builder = SUVCarBuilder()
    director = CarDirector(suv_car_builder)
    director.construct_car()
    suv_car = director.get_car()
    print("SUV Car:", suv_car)
 