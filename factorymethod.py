from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def create_product(self, kind=None):
        pass


class AnimalFactory(Factory):
    def create_product(self, kind=None):
        if kind == "dog":
            return Dog()
        elif kind == "cat":
            return Cat()
        else:
            return None


class DogFactory(Factory):
    def create_product(self, kind=None):
        return Dog()


class CatFactory(Factory):
    def create_product(self, kind=None):
        return Cat()

class Animals(ABC):
    @abstractmethod
    def run(self):
        pass

class Dog(Animals):
    def run(self):
        print("I'm a Dog, I can run!!")

class Cat(Animals):
    def run(self):
        print("I'm a Cat, I can run!!")



factory = DogFactory()
dog = factory.create_product()
dog.run()

factory = CatFactory()
cat = factory.create_product()
cat.run()

animal_factory = AnimalFactory()
animal1 = animal_factory.create_product("dog")
animal2 = animal_factory.create_product("cat")
animal3 = animal_factory.create_product("lion")  # Invalid kind

animal1.run()
animal2.run()



# factory = DogFactory()
# dog = Dog()  
# dog = factory.create_product() 
# dog.run()  
 
# client
# factory = DogFactory()
# dog = Dog()
# dog = factory.create_product()
 
# dog.run()

