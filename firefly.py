class Firefly:
    #function that inputs "time" in some discrete units and outputs proportion of "charge"
    #start with lets say a log scale, so it curves the correct way
    #sets a flag to say if it lights up
    #in main, every cycle it checks how many flags are set and adds a constant value to each firefly charge
    #need a private variable to store charge. Lets say charge varies from 0-100
    #what is the "leakiness"? is that captured in the log charging curve?
    #the charging curve increments along based on the current charge?

    charge = 0
    id_num = ''

    def __init__(self, id_num, initial_charge):
        self.id_num = id_num
        self.charge = initial_charge
        

    