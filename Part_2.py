'''
from Part_1 import JazzMusician, dude_1, dude_2
import Part_1 
'''
#^ if you want to import classses from another file into a separate file

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
        #self.aura = People.aura + self.nonchalance       people.aura would never change

    


dude_1 = People('Mike', 'Wazowski', 1)
dude_2 = People('Pepe', 'Ariano', 10)

People.num_of_people +=1
print("Number of people = {}".format(People.num_of_people))

for i in range(5):
    print("Current aura is {}".format(dude_1.aura_check()))
    print("Adding....")
    dude_1.aura_farm()
    print("New aura is {}".format(dude_1.aura_check()))

'''
print(dude_1.__dict__)      #using dict is a powerful tool to see inside objects, and classes
dude_1.num_of_people = 400 
print(dude_1.__dict__). #after manually changing dude_1's specific num_of_people, dude_1 has an extra addition into it's dictionary, before it is assumed dude_1.num_of_people is the same as People.num_of_people


dude_1.swag = 100     adding another attribute after initialization is called monkey patching but isn't recommended?
'''

