'''
from Part_1 import JazzMusician, dude_1, dude_2
import Part_1 
'''
#^ if you want to import classses from another file into a separate file

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
    
    #def aura_farm(self):



dude_1 = People('Mike', 'Wazowski', 1)
dude_2 = People('Pepe', 'Ariano', 10)
'''
print(dude_1.__dict__)
print(dude_1.__dict__)
print(People.__dict__)
'''
#dude_1.swag = 100     adding another attribute after initialization is called monkey patching but isn't recommended?

print(dude_1.__dict__)

#print(dude_1.aura_check())
#print(dude_2.aura_check())