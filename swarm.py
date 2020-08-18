import abc

import firefly

class Swarm:

    size = 0
    fireflies = []
    whosFlashing = []

    def __init__(self, size):
        self.size = size
        self._observers = set()

        for index in range(size):
            f = firefly.Firefly(index, 10*index)
            self.fireflies.append(f)
            self.whosFlashing.append(False)
            self._observers.add(f)
            f._subject = self

    def _notify(self):
        for observer in self._observers:
            observer.update(self.whosFlashing)

    @property
    def subject_state(self):
        return self.whosFlashing
    
    @subject_state.setter
    def subject_state(self, arg):
        index = 0
        while(index < self.size):
            if(not whosFlashing[index]):
                index += index
            if(whosFlashing[index]):
                self._notify()
                whosFlashing[index] = False
                index = 0
        


        for fly in self.fireflies:
           if(fly.checkFlash(self.whosFlashing)):
                self._notify()
        

    def chargeIteration(self):
        for fly in self.fireflies:
            fly.charging()

    def checkFlash(self):
        #checks each firefly, updating their isFlashing values and stores in local list
        for fly in self.fireflies:
            fly.checkFlash(self.whosFlashing)

    def flashPropogation(self):
        for fly in self.fireflies:
            fly.charge += 10

    def flashPropogationLoop(self):
        for fly in self.fireflies:
            #if any fly is flashing
            if(fly.isFlashing):
                #additive effect to all other fireflies
                self.flashPropogation()
                #checks all fireflies for new flashers
                self.checkFlash()

        #uses charge>100 as the qualifier for flashing, after all the checks then resets these charges to the correct value 0
        for fly in self.fireflies:
            if(fly.isFlashing):
                fly.charge = 0

    def addFlashData(self):
        for fly in self.fireflies:
            fly.flashData.append(fly.charge)

    def plotChargeData(self, ax, id_num):
        ax.plot(range(0, len(self.fireflies[id_num].chargeData)), self.fireflies[id_num].chargeData)

    def plotFlashData(self, ax, id_num):
        ax.plot(range(0, len(self.fireflies[id_num].flashData)*19, 19), self.fireflies[id_num].flashData)

    