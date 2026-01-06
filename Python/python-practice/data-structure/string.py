userinput = int(input("Enter a number : "))

aCount = 0
eCount = 0
iCount = 0
oCount = 0
uCount = 0
consonentCount = 0

for i in range(len(string)):
    if(string == 'a'):
       aCount += 1
    elif(string == 'e'):
       eCount += 1
    elif(string == "i"):
      iCount += 1
    elif(string == "o"):
      oCount += 1
    elif(string == "u"):
      uCount += 1
    else:
      consonentCount = 1


print("A count :", aCount)
print("E count :", eCount)
print("I count :", iCount)
print("O count :", oCount)
print("U count :", uCount)
print("consonent count:", consonentCount)