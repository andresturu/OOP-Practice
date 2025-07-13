class JazzMusician:
    
    def __init__(self, first, last, nickname, instrument):  #self is called the instance
        self.fname = first #normll would just do self.first = first but I'm just seeing if this works too
        self.lname = last #normally would just do self.last = last but I'm just seeing if this works
        self.nname = nickname
        self.instrument = instrument #these are instance varaibles, also known as attributes
    
    def player_introduction(self): #this is a method
        return '{} "{}" {}'.format(self.fname, self.nname, self.lname) #helpful tool for easier sentence construction .format

#dude_1 is the instance argument 
dude_1 = JazzMusician('Greg', 'Heffley', 'The heffler', 'Drums')
dude_2 = JazzMusician('Bill', 'Mackers', 'Chop-tone', 'Saxophone')

'''
print(dude_1.player_introduction())
print(JazzMusician.player_introduction(dude_1))# these two are equivalent
print(dude_2.player_introduction())
'''
