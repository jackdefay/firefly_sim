import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import swarm

s1 = swarm.Swarm(2)

fig, ax = plt.subplots()

for fly in s1.fireflies:
    print(fly.id_num)

duration = 200

for time in range(duration):
    s1.fireflies[0].charging()
    if(s1.fireflies[0].isFlashing):
        s1.addFlashData()
        s1.fireflies[1].charge += 10
    s1.fireflies[1].charging()


s1.plotChargeData(ax, 0)

plt.show()