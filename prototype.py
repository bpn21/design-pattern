from abc import ABC, abstractmethod
import copy


class Document(ABC):
    @abstractmethod
    def clone(self):
        pass


class Report(Document):
    def __init__(self):
        self.quartar = "1st Quartar"
        self.symbol = "HDL"
        self.aurthor = None

    def __str__(self):
        return f"This is the report by {self.aurthor} about {self.quartar} of symbol {self.symbol}"

    def clone(self):
        return copy.deepcopy(self)


def client_code():
    report1 = Report()
    report2 = report1.clone()
    report2.aurthor = "Rajesh Puri"
    report3 = report1.clone()
    report3.aurthor = 'Suraj'
    print(report1)
    print(report2)
    print(report3)


client_code()


# # Shallow Copy
# # copy.copy(orginal list) This is shallow copy that changes the orginal list


# def test(arr):
#     arr1 = arr
#     arr1 = ["python"]  # reassignment of arr1 doesn't alter arr.
#     print(arr1)
#     arr1 = ["java"]  # reassignment of arr1 doesn't alter arr.
#     arr1[0] = "new language"
#     print(arr1)
#     arr[0] = "typescript"  # modification will alter orginal arr


# arr = ["javascript"]

# test(arr)
# print(arr)
