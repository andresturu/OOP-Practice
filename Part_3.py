
#this will showcase class methods and static methods


import time

class People:

    #instance_lst= [] in case you want to have a list of all of the instances and loop over them
    aura = 100
    num_of_people = 0
    
    def __init__(self, fname, lname, nonchalance):
        self.fname = fname
        self.lname = lname
        self.nonchalance = nonchalance
        People.num_of_people += 1 #access class variable through class rather than self when this a variable that wouldn't ever be changed depending on the person
       # People.instance_lst.append(self) #adds instance to list

    def aura_check(self):
        return '{} {} has {} aura'.format(self.fname, self.lname, self.aura)
    
    def aura_farm(self):
        self.aura += self.nonchalance
        

    def grow_aura(self, days):
        for i in range(days):
            print("Day {}: {} {} has {} aura".format(i+1, self.fname, self.lname, self.aura))
            print('Adding..')
            time.sleep(2)
            self.aura_farm() #calling a method within a method 
            print("End of Day {}: {} {} now has {} aura".format(i+1, self.fname, self.lname, self.aura))


    @classmethod
    def is_large_amt_ppl(cls):
        if People.num_of_people >10:
            return True
        return False

    @classmethod #this is the decorator, conventional to name alternative constructors 'from....'
    def from_string(cls, person_string): #'cls' is passed automatically, similar to 'self'
        first, last, nonchalance = person_string.split('-') #split creates a list of the elements between '-' in the string, you can actually unpack a list like so^, the list has three elements and you're assigning variables to each element respectively
        return cls(first, last, nonchalance) #this entire function/classmethod is called an alternative constructor because it allows you to create more objects
   
    @staticmethod
    def affirmation(): #static methods do not have an automatic arguement/paramter unlike class and regular methods
        print("aura is made up anyway")

dude_1 = People('Mike', 'Wazowski', 1)
dude_2 = People('Pepe', 'Ariano', 10)

intro_str_3 = 'Jose-Dorado-20'
intro_str_4 = 'Harry-Putnam-3'
dude_3 = People.from_string(intro_str_3) #using an alternative constructor to make a new object
dude_4 = People.from_string(intro_str_4)


#People.grow_aura(dude_2, 4) #calling it through people
dude_2.grow_aura(4)



#print(People.instance_lst)
print(People.is_large_amt_ppl()) #returns True or False depending if amount of instances is >10
People.affirmation()