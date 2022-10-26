def runner_up(list):
    list = sorted(list)
    list = list[::-1]
    list = list[1]
    return list
def runup():
    list = [17, 22, 36, 14, 5]
    print(runner_up(list))
runup()
