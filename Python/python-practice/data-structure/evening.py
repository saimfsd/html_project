basic = 5000
 
da = 0.21 * basic      # 21%
hra = 0.15 * basic     # 15%
ta = 0.05 * basic      # 5%
insurance = 500        # fixed
pf = 0.12 * basic      # 12%
 
gross = basic + da + hra + ta
net = gross - (pf + insurance)
 
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("Gross Salary:", gross)
print("PF:", pf)
print("Insurance:", insurance)
print("Net Salary:", net) 


# n = int(input("Enter n: "))
# sum_series = 0

# for i in range(1,n+1):
#     sum_series += i/(i + 1)

#     print("Sum of series =", sum_series)


# x = float(input("Enter value of x: "))
# n = int(input("Enter value of n: "))

# sum = 0
# i = 1

# while i <= n:
#     sum += x / i
#     i += 1

# print("Sum of series =", sum)





# n = int(input("Enter value of n: "))

# a = 3/(3+1)
# sum = 0
# i = 1

# while i <= n:
#     sum += i / (i + 1)
#     i += 1

# print("Sum of series =", sum)






# s = input("Enter string: ")
# vowels = "aeiouAEIOU"

# count = 0
# i = 0

# while i < len(s) - 1:
#     if s[i] in vowels and s[i+1] in vowels:
#         count += 1
#     i += 1

# print("Two successive vowels occur", count, "times")





# n = int(input("Enter value of n: "))

# series = ""
# sum = 0

# for i in range(1, n + 1):
#     sum += i / (i + 1)
#     series += f"{i}/{i+1}"
#     if i != n:
#         series += " + "

# print("Series:", series)
# print("Sum of series =", sum)




# array = [1, 2, 4, 6, 1, 2]

# newArray = []
# for x in array:
#     if x not in newArray :
#        newArray.append(x)

# print("Array without duplicates =", newArray )


# array = [1, 2, 4, 6, 1, 2]
# newArray = []

# for i in range(len(array)):
#     if array[i] not in newArray:
#         newArray.append(array[i])

# print(newArray)



