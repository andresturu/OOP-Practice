class Vehicle:
    #instance methods, class methods, static methods
    
    def __init__(self, name, num_wheels, speed, max_fuel):
        self.name = name
        self.num_wheels = num_wheels
        self.speed = speed
        self.max_fuel = max_fuel


    def remind_fuel(self):
        if self.fuel_level < .25 * self.max_fuel:
            print("Your fuel is low, recharge")


class Truck(Vehicle):

    def __init__(self, name, num_wheels, speed, max_fuel, fuel_level):
        super().__init__(name, num_wheels, speed, max_fuel)
        self.fuel_level = fuel_level

truck_1 = Truck('mater', 4, 100, 30, 0)

truck_1.remind_fuel()