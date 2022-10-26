import time

def randFunc(iterations: int) -> str:
    myVar = str()
    for x in range(int(iterations)):
        temp = (((time.time_ns() **0.856) % 6) + 1)
        myVar += str(int(temp))
        #temp = myVar
        #print(myVar)
        time.sleep((temp % 3 / 1300))

    return myVar

randFunc(5)
