class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display(self):
        print(f"Brand: {self.brand}, Color: {self.color}")
        
my_car = Car("Koenigsegg Jesko", "Yellow")
my_car.display()