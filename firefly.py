import numpy as np

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
    isFlashing = False

    chargeData = []
    flashData = []

    def __init__(self, id_num, initial_charge):
        self.id_num = id_num
        self.charge = initial_charge

        self.isFlashing = False
        self.chargeData = []
        self.flashData = []
        

    def log(self, x):
        return np.ceil(np.log(x+1))

    def sqrt(self, x):
        return np.ceil(np.sqrt(x+1))

    def checkFlash(self):
        if(self.charge >= 100):
            self.isFlashing = True
        else:
            self.isFlashing = False

    def charging(self):
        #adds to charging curve based on incremental value defined by charging curve and the current value
        self.charge = self.charge + self.sqrt(self.charge)
        #checks if the fly is flashing so the swarm function can propogate it
        self.checkFlash()
        #zeros out the charge if it is
        if(self.isFlashing):
            self.charge = 0
        #keeps a log of charge data
        self.chargeData.append(self.charge)

    