from abc import ABC, abstractmethod


class BakeCake(ABC):
    @abstractmethod
    def Bake():
        pass


class VanillaCake(BakeCake):
    def Bake(self):
        print("Baking Vanilla Cake")


class StrawberryCake(BakeCake):
    def Bake(self):
        print("Baking Strawerry Cake")


class MochaCake(BakeCake):
    def Bake(self):
        print("Backing Mocha Cake")


class ChocolateCake(BakeCake):
    def Bake(self):
        print("Bake Chococlate Cake")


class CakeFactory:
    # def __init__(self):
    #     self.cake_type = input("Enter the cake type")
    def create_cake(cake_type):
        TYPES = {
            "vanilla": VanillaCake,
            "mocha": MochaCake,
            "chocolate": ChocolateCake,
            "strawberry": StrawberryCake,
        }

        if cake_type not in TYPES:
            raise ValueError(f"{cake_type} is not avaliable")

        obj = TYPES[cake_type]()
        # with () paranthesis, object is initiated, without obj we cant access methods inside any classes.
        return obj


# Client Side
def order_cake(cake_type):
    cake = CakeFactory.create_cake(cake_type)
    return cake


order_cake("mocha").Bake()
