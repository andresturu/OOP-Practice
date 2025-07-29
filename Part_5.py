#learned about special methods

class Person:

    def __init__(self, fname, lname, occupation, salary): #__init__ is a special method
        self.fname = fname
        self.lname = lname
        self.occupation = occupation
        self.salary = salary

    def fullname(self):
        return f'{self.fname} {self.lname}'

    def __repr__(self):  #a special mthod too
        return "Person('{}', '{}', '{}', '{}')".format(self.fname, self.lname, self.occupation, self.salary)
    #repr is for the developer's use. Meant to be used for debugging and for object recreation
    #notice how I put quotes around the attributes, to clearly indicate to the developr that the attributes are strings
   
    def __str__(self):
        return "{} {} is a {} with a salary of {}".format(self.fname, self.lname, self.occupation, self.salary)
    #str is meant to prettily represent an object to the user

    def __add__(self, other): #say when we want to add two instances we get their combined salaries
        return self.salary + other.salary, self.occupation + other.occupation   #__add__ also deals with concatenating strings
    
    def __len__(self): #len is a special method too
        return len(self.fullname())
 
p1 = Person('Andres', 'Turullols', 'Unemployed', 10)
p2 = Person('Arielle', 'Turullols', 'Software Intern', 1500)

print(len(p1))

combined_salary, combined_job_title = p1 + p2 #here we redefine how to add objects
print(combined_salary)
print(combined_job_title)

print(p1 + p2)
print(Person.__add__(p1, p2)) #also calls __add__ with the same result


print(p1) #defaults to str

print(repr(p1)) #these have the same output
print(p1.__repr__())

print(str(p1)) #these have the same output
print(p1.__str__())

