string = input("Enter a string : ")
isPresent = False
SpecialChar = False


for i in range(len(string)):
    if (string[i] <= '0' and string[i] >= '9'):
       isPresent = True
    if(string[i] == '@' or string[i] == '!'  or string[i] == '#'):
        SpecialChar = True
    if(string[i] >= 'A' and string <= 'z'):
        print("Upper case is present:")

if(isPresent and SpecialChar):
    print("String contain a number and special character")
elif(isPresent):
    print("sttring contains a number")
elif(SpecialChar):
     print("sttring contains a special charecter")
else:
    print("string dosen't contain a number")

    