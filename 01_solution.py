class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1 

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"The car brand is: {self.__brand} and this is the Model: {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are Cool"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"
 
my_Tesla = ElectricCar("Tesla", "Model S", 100)

print(isinstance(my_Tesla, ElectricCar))  
print(isinstance(my_Tesla, Car)) 

class Battery:
    def battery_info(self):
        return "This is a 100kWh battery"

class Engine:
    def engine_info(self):
        return "This is a 2000cc engine"

class ElectricCarTwo(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call the constructor of the Car class
        self.battery_size = battery_size  # Add the additional argument

myNewTesla = ElectricCarTwo("Tesla", "Model X", 120)
battery_instance = Battery()
engine_instance = Engine()

print(battery_instance.battery_info())
print(engine_instance.engine_info())