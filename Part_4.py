class Vehicle:
    #instance methods, class methods, static methods
    
    def __init__(self, name, speed, curr_fuel_level):
        self.name = name 
        self.speed = speed
        self.curr_fuel_level = curr_fuel_level

        ''' if curr_fuel_level == None:
            self.curr_fuel_level = max_fuel #if no arguement is given assume the vehicle is at full 
        else:
            self.curr_fuel_level = curr_fuel_level'''


    def remind_fuel(self):
        if self.curr_fuel_level < .25 * self.max_fuel:
            print("Your fuel is low, refuel soon")
        else:
            print("No need to refuel yet")

    @staticmethod
    def give_num_wheels(obj):  #this is a static method! Because it doesn't use self, nor does it access the Vehicle class automatically, instead I am handing it the subclass information explicitly
        if isinstance(obj, Vehicle):  #checks if obj is an instance, for example semitruck_1 is an instance 
            cls = obj.__class__ #get's the class of the instance
        else:
            cls = obj   #if obj is not an instance, we're assuming it's a subclass so we can just set cls = obj
        print(cls.num_wheels)

class SemiTruck(Vehicle):
    num_wheels = 4 #class variable because all semitrucks should have 4 wheels
    max_fuel = 100. #Gonna say all semitrucks have a max_fuel of 100
    def __init__(self, name, speed, curr_fuel_level = max_fuel): #by defualt current fuel level will be max fuel unless specified in an additional paramater
        super().__init__(name,speed, curr_fuel_level)

class EBike(Vehicle):
    num_wheels = 2
    max_fuel = 20
    def __init__(self, name, speed, curr_fuel_level = max_fuel): 
        super().__init__(name,speed, curr_fuel_level)


semitruck_1 = SemiTruck('mater', 65, 50) #optional curr_fuel_level arguement that I didn't specify here
semitruck_1 = SemiTruck('darryl', 75)
ebike_1 = EBike("John", 30)

ebike_1.remind_fuel()





'''
Vehicle.give_num_wheels(SemiTruck)        #all versions of these work
Vehicle.give_num_wheels(semitruck_1)
SemiTruck.give_num_wheels(semitruck_1)
SemiTruck.give_num_wheels(SemiTruck)
semitruck_1.give_num_wheels(SemiTruck)
semitruck_1.give_num_wheels(semitruck_1)
'''
#print(help(truck_1))  useful tool