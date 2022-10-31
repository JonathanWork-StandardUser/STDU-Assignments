from random import randint
import matplotlib.pyplot as plt
import numpy as np

myList = []
for x in range(100):
    #print(x)
    myList.append(randint(1, 6))

print(myList, len(myList))
plt.plot(myList)
plt.xlabel('Iterations')
plt.ylabel('Dice Rolls')
plt.savefig("static\images\plot.png")
#plt.show()
