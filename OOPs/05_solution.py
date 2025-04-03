@
class Car:
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "pertol" or "diesel" 
        
my_car = Car("Toyota", "corolla")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"
        
my_electric_car = ElectricCar("tesla", "Model S", "85KWH")

print(my_electric_car.fuel_type())

safari = Car("tata", "safari")
print(safari.fuel_type())

