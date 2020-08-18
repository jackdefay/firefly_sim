import firefly

class Swarm:

    size = 0
    fireflies = []

    def __init__(self, size):
        self.size = size

        for index in range(size):
            f = firefly.Firefly(index, 10*index)
            self.fireflies.append(f)


    def addFlashData(self):
        for fly in self.fireflies:
            fly.flashData.append(fly.charge)

    def chargeIteration(self):
        for fly in self.fireflies:
            fly.charging()

    def checkFlash(self):
        for fly in self.fireflies:
            fly.checkFlash()

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


    def plotChargeData(self, ax, id_num):
        ax.plot(range(0, len(self.fireflies[id_num].chargeData)), self.fireflies[id_num].chargeData)

    def plotFlashData(self, ax, id_num):
        ax.plot(range(0, len(self.fireflies[id_num].flashData)*19, 19), self.fireflies[id_num].flashData)

    