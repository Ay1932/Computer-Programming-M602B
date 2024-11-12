#Ex-1
class Animal():
    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def speak(self):
        print("I am a dog.")
        
animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

#Ex-2
class Shape:
    def area(self):
        return 0
    
class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
rectangle = rectangle(5,3)
triangle = triangle(3,5)

print("Rectangle area:", rectangle.area())
print("Triangle area:", triangle.area())


#Ex-3
class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year
        
    def get_info(self):
        return f"Year: {self.year}, Make: {self.make}, Model: {self.model}"    
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year
        
    def get_info(self):
        return f"Year: {self.year}, Make: {self.make}, Model: {self.model}"    
    
car = Car("Volkwagen", "Polo", 2015)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019)

print(car.get_info())       
print(motorcycle.get_info())