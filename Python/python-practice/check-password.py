
string = str(input("Enter your password : "))

isNumberPresent = False
isPresentSpecialChar = False
isCharPresent = False

for i in range(len(string)):
    if(string[i] >= '0' and string[i] <= '9'):
        isNumberPresent = True

    if(string[i] == '#' or string[i] == '@' or string[i] == '$' or string[i] == '%'):
        isPresentSpecialChar = True

    if(string[i] >= 'a' and string[i] <= 'z' or string[i] >= 'A' and string[i] <= 'Z'):
        isCharPresent = True


if(isPresentSpecialChar == True and isNumberPresent == True and isCharPresent == True):
    print("Password is strong, number and special character is present")

elif(isPresentSpecialChar == True):
    print("Password is weak, special character is present")

elif(isNumberPresent == True):
    print("Password is weak, number is present")

elif(isCharPresent == True):
    print("Password is strong, character is present")

else:
    print("Password is weak")