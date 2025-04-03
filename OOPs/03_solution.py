class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        

my_car = Car("Toyota", "corolla")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size
        
my_electric_car = ElectricCar("tesla", "Model S", "85KWH")
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_size)

