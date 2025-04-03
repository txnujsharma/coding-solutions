
class Car:
    total_count = 0
    def __init__(self, brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_count += 1

    def get_brand(self):
        return self.__brand + " !"
    
    @property
    def model(self):
        return self.__model
    
    def fuel_type(self):
        return "pertol" or "diesel" 
    
    @staticmethod
    def description():
        return "it is a amazing car"
        
my_car = Car("Toyota", "corolla")
print(my_car.description())
print(Car.description())
print(my_car.model)

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand , model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "electric charge"
        
# my_electric_car = ElectricCar("tesla", "Model S", "85KWH")



# print(my_electric_car.fuel_type())

# safari = Car("tata", "safari")

# safari_1 = Car("tata", "safari_1")

# safari_2 = Car("tata", "safari_2")
# test = Car("test", "test")
# print(Car.total_count)

