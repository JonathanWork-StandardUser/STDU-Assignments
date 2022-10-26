from flask import Flask, render_template, request
from randNum import randFunc
from toDict import fileToDict
from random import randint
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def randDice():
    myDict = fileToDict("words.txt")
    randWords = []
    randNum = []
    for x in range(5):
        randList = randFunc(5)
        print(int(randList), type(int(randList)))
        randWords.append(myDict[randList])
        randNum.append(randList)

    return render_template('randDice.html', randWords = randWords, numbers = randNum)
#
#@app.route("/swap", methods = ["GET", "POST"])
#def swapCase():
#    if request.method == "POST":
#        first
#
@app.route("/swapCase")
def swapCase():
    myString = input("Enter string here por favor: ")
    outString = ""
    for x in myString:
        #print(x)
        if(x.isupper()):
            #print("B4 Capital Letter: " + x)
            outString += x.lower()
            #print("After lower Letter: " + x)
        else:
            #print("B4 Lowercase Letter: " + x)
            outString += x.upper()
            #print("After Capital Letter" + x)
        
    return(outString)

@app.route("/plotDice")
def plotDice():
    myList = []
    for x in range(100):
        #print(x)
        myList.append(randint(1, 6))

        print(myList, len(myList))
        plt.plot(myList)
        plt.xlabel('Iterations')
        plt.ylabel('Dice Rolls')
    return(render_template('plotDice.html', imageName = 'plot.png'))

#@app.route("/tryForms", methods=())

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=9001)