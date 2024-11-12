class Vehicle:
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

# Example usage
car = Car("Toyota", "Camry", 2022)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021)

print(car.get_info())          # Outputs: Year: 2022, Make: Toyota, Model: Camry
print(motorcycle.get_info())    # Outputs: Year: 2021, Make: Harley-Davidson, Model: Street 750
