array = [
    [1,2,3],
    [2,5,7]
]


print(array[0][0])
print(array[0][1])
print(array[0][2])
print(array[1][0])
print(array[1][1])
print(array[1][2])

array[1][0] = 10

print("Using for loop-----------------")
for i in range(len(array)):
    row = ""
    for j in range(len(array[i])):
        row += str(array[i][j])+" "
        print(row)