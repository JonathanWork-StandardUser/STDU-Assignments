
def fileToDict(filename: str) -> dict:
    myDict = {}

    myFile = open(filename)
    for line in myFile:
        key, value = line.split()

        #print(key, value)
        myDict[key] = value

    return myDict

fileToDict("words.txt")