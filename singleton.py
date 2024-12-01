# __new__ is a inbuild mehthod in pythion that is responsible of creating an instance, __init__ then initilizes the created instance by __new__, So whenever, the objected is created using Class, it creates instance every single time. So we have to go and rewrite the __new__ method and stop creation of instance of that particular class if the instance as already created. This makes single instance of a class and so this method is called singleton method.
# HINTS:  For this we make a attribute/variable in class level to store a instance of a class and return it.


class DatabaseConnection:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # Always creates a new Instance /Violets Singleton


db1 = DatabaseConnection()
db2 = DatabaseConnection()
# db1 is not equal to db2 // Different instance

# =======================================


class DatabaseConnection:
    _instance = None  # Class level attribute to store the single instance

    def __new__(cls, *arg, **kwargs):
        if cls._instance in None:
            cls._instance = super().__new__(cls)
            return cls._instance


singleton1 = DatabaseConnection()
singleton2 = DatabaseConnection()

# Here, singleton1 and singleton2 are equal. they both are same instance
