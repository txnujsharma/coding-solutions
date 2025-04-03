class Car:
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"
        
my_car = Car("Toyota", "corolla")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size
        
my_electric_car = ElectricCar("tesla", "Model S", "85KWH")

print(my_car.get_brand())

