arr = [
    [2, 4, 6],
    [3, 5, 7]
]
 
print(arr[0][0])
print(arr[0][1])
print(arr[0][2])
print(arr[1][0])
print(arr[1][1])
print(arr[1][2])

for i in range(len(arr)):
    for j in range(len(i)):
        print([i][j])


# arr[0][1] = 40
# arr[1][2] = 70

 
# print("arr[0][2] =", arr[0][2])  
# print("arr[1][0] =", arr[1][0])  

 
# for row in arr:
#     print(row)
55