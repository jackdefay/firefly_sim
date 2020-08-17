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

    def plotChargeData(self, ax, id_num):
        ax.plot(range(0, len(self.fireflies[id_num].chargeData)), self.fireflies[id_num].chargeData)

    def plotFlashData(self, ax, id_num):
        ax.plot(range(0, len(self.fireflies[id_num].flashData)*19, 19), self.fireflies[id_num].flashData)

    