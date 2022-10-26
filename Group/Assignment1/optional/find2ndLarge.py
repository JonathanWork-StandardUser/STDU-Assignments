import argparse

parser = argparse.ArgumentParser()
parser.add_argument("length", type = int, help="Enter length of password to be.", nargs = "+")
args = parser.parse_args()

print(args)
myList = args.length
print(len(myList))
largest = myList[0]
large2 = myList[1]
for x in myList:
    if x > largest:
        large2 = largest
        largest = x
        #print(large2, largest)
    elif x > large2:
        large2 = x

print(myList)
print(large2)
#for x in args