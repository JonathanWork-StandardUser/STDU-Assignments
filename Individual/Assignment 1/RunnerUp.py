def runner_up(numbr):
    numbr = sorted(numbr)
    numbr = numbr[::-1]
    numbr = numbr[1]
    return numbr
def runup():
    numbr = [17, 22, 36, 14, 5]
    print(runner_up(numbr))
runup()
