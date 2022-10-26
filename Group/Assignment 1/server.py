from flask import Flask, render_template, jsonify
from randNum import randFunc
from toDict import fileToDict

app = Flask(__name__)

@app.route('/')
def randDice():
    myDict = fileToDict("words.txt")
    randWords = []
    for x in range(5):
        randList = randFunc(5)
        print(int(randList), type(int(randList)))
        randWords.append([randList, myDict[randList]])

    jsonObj = jsonify(randWords)
    print(randWords)
    print(jsonObj)
    return render_template('randDice.html', randWords = randWords)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=9001)