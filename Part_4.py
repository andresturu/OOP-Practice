class Vehicle:
    #instance methods, class methods, static methods
    
    def __init__(self, name, speed, max_fuel, curr_fuel_level = None):
        self.name = name
        self.speed = speed
        self.max_fuel = max_fuel
        if curr_fuel_level == None:
            self.curr_fuel_level = max_fuel
        else:
            self.curr_fuel_level = curr_fuel_level


    def remind_fuel(self):
        if self.curr_fuel_level < .25 * self.max_fuel:
            print("Your fuel is low, refuel soon")
        else:
            print("No need to refuel yet")


class SemiTruck(Vehicle):
    num_wheels = 4 #class variable because all semitrucks should have 4 wheels
    def __init__(self, name, speed, max_fuel, curr_fuel_level):
        super().__init__(name,speed, max_fuel, curr_fuel_level)

truck_1 = SemiTruck('mater', 100, 30, 5)

truck_1.remind_fuel()