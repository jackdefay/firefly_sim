import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import swarm

s1 = swarm.Swarm(3)

fig, ax = plt.subplots()

for fly in s1.fireflies:
    print(fly.id_num)

duration = 100

for time in range(duration):
    s1.chargeIteration()
    s1.flashPropogationLoop()


s1.plotFlashData(ax, 0)
s1.plotFlashData(ax, 1)
s1.plotFlashData(ax, 2)

plt.show()