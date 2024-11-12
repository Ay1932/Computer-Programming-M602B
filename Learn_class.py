class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example usage
person1 = Person("Alice", 30)
person2 = Person("Adrian", 33)
person3 = Person("Martha", 25)
person1.greet()
person2.greet()
person3.greet()

#Ex-2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

#Ex-3
class Bankaccount:
    def __init__(self,initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Amount must be in positive.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Withdraw amount must be positive.")
        
account = Bankaccount(100)  # Initial balance of 100
account.deposit(50)
account.withdraw(30)
account.withdraw(100)


#Ex-4
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.year} {self.make} {self.model}")

# Example usage
car = Car("Toyota", "Camry", 2022)
car.description()