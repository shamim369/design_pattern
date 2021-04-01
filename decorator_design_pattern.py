# Decorator Design Pattern
from abc import ABC, abstractmethod
class Model(ABC):

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def set_age(self, age):
        pass
    
    @abstractmethod
    def get_age(self):
        pass

class Alice(Model):
    name = "Alice"
    age = 23

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Badhon(Model):
    
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Lipstick(Model):

    def __init__(self, model):
        self.model = model
        self.name = self.model.get_name()
        self.age = self.model.get_age()

        self.age = self.age + 1
        self.name = self.name + " with lipstick"

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Eyeliner(Model):

    def __init__(self, model):
        self.model = model
        self.name = self.model.get_name()
        self.age = self.model.get_age()

        self.age = self.age - 2
        self.name = self.name + " with Eyeliner"

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Main:
    model = Alice()
    model = Lipstick(model)
    print(model.get_name())
    print(model.get_age())

    badhon = Badhon()
    badhon.set_name('Akramuzzaman Badhon')
    badhon.set_age(20)
    model = Lipstick(badhon)
    print(model.get_name())
    print(model.get_age())

    badhon = Badhon()
    badhon.set_name('Akramuzzaman Badhon')
    badhon.set_age(20)
    model = Eyeliner(badhon)
    print(model.get_name())
    print(model.get_age())

if __name__ == '__main__':
    Main()