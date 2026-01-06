import math
num = int(input("Enter a number: "))

value = num
sum = 0
product = 1
while(value > 0):
    temp = value % 10
    sum = sum + temp
    product = product * temp
    value = math.floor(value / 10)

    print(sum)
    print(product)