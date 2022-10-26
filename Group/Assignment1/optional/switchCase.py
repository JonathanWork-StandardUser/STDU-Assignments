print("something")

myString = input("Enter string here por favor: ")
outString = ""
for x in myString:
    print(x)
    if(x.isupper()):
        print("B4 Capital Letter: " + x)
        outString += x.lower()
        print("After lower Letter: " + x)
    else:
        print("B4 Lowercase Letter: " + x)
        outString += x.upper()
        print("After Capital Letter" + x)
    
print(outString)