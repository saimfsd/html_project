# num = int(input("Enter a value: "))
# summ = 0
# series = ""   # yaha series store hogi

# for i in range(1, num + 1):
#     summ += i / (i + 1)

#     series += f"{i}/{i+1}"   # series string me add kar rahe
#     if i != num:
#         series += " + "      # beech me + add karna hai

# print("Series =", series)
# print("Final answer =", summ)


sum = 0
x = int(input("Enter x value: "))
n = int(input("Enter n value: "))

for i in range(1, n + 1):
    sum += x / i
    print(f"{x}/{i} +", end=" ")   # same line me print hoga

print("\nFinal Sum =", sum)


      