# number = int(input("Enter a number : "))

# product = 1

# for i in range(1, number):
#     product = product * i

# print(product)

# number = int(input("Enter a number : "))

# product = 1

# for i in range(1, number + 1):
#     product *= i
#     print(i, end=" x " if i < number else " = ")

# print(product)


number = int(input("Enter a number : "))

product = 1
string = ""

for i in range(1, number + 1):
    product *= i
    string += str(i)
    if(i < number):
        string += " x "
    else:
        string += " = " 

    print(str(product))
 