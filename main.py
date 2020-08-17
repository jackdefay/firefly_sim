import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import firefly

f1 = firefly.Firefly('f1', 0)
f2 = firefly.Firefly('f2', 10)

fireflies = [f1, f2]

fig, ax = plt.subplots()

print(f1.id_num) #change to cycle all ids

def addFlashData():  #change to cycle all ids
    f2.flashData.append(f2.charge)

duration = 200

for time in range(duration):
    f1.charging()
    if(f1.isFlashing):
        f2.charge += 10
    f2.charging()

# print(f1.chargeData)

ax.plot(range(0, duration), f1.chargeData, linewidth=3)
ax.plot(range(0, duration), f2.chargeData)
# ax.scatter(range(0, len(f2.flashData*19), 19), f2.flashData)

plt.show()