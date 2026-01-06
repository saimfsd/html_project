import math

nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

a = int(input("Enter a number: "))

for i in range(13):
    value = math.floor(a / nums[i])
    for j in range(value):
        print(romans[i-1], end="")
    a = a % nums[i]   # reduce the number for next stepsS