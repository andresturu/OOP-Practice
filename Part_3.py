
#this will showcase class methods and static methods


import time

class People:

    aura = 100
    num_of_people = 0
    
    def __init__(self, fname, lname, nonchalance):
        self.fname = fname
        self.lname = lname
        self.nonchalance = nonchalance
        People.num_of_people += 1 #access class variable through class rather than self when this a variable that wouldn't ever be changed depending on the person

    def aura_check(self):
        return '{} {} has {} aura'.format(self.fname, self.lname, self.aura)
    
    def aura_farm(self):
        self.aura += self.nonchalance

    @classmethod #this is the decorator, conventional to name alternative constructors 'from....'
    def from_string(cls, person_string): #'cls' is passed automatically, similar to 'self'
        first, last, nonchalance = person_string.split('-') #split creates a list of the elements between '-' in the string, you can actually unpack a list like so^, the list has three elements and you're assigning variables to each element respectively
        return cls(first, last, nonchalance) #this entire function/classmethod is called an alternative constructor because it allows you to create more objects
   
    @staticmethod
    def add(x,y):
        return x +y

dude_1 = People('Mike', 'Wazowski', 1)
dude_2 = People('Pepe', 'Ariano', 10)

intro_str_3 = 'Jose-Dorado-20'
dude_3 = People.from_string(intro_str_3) #using an alternative constructor to make a new object




print(People.add(2,4))


for i in range(5):  #I think this could be a static method
    print("Current aura is {}".format(dude_1.aura_check()))
    print("Adding....")
    time.sleep(0.5)
    dude_1.aura_farm()
    print("New aura is {}".format(dude_1.aura_check()))



