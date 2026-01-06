# Assign Array
# Read Array
# Print Array
# Create Array

# Update 
# Delete
# Search

# Addition
# Subraction
# Multiplication

# Transpose
# Sort

# Row wise Sum
# Column wise sum


array = [
    [5,6,7],
    [1,2,3],
    [9,8,7]
]

array[2][1] = 10
array[2][2] = 0

# array[2].remove(7)

for i in range(3):
    row = ""
    for j in range(3):
        row += str(array[i][j])+ " "
    print(row)

    search = int(input("Enter a value for search : "))

    isPresernt = False

    a = 0
    b = 0
    for i in range(3):
        for j in range(3):
            if(array[i][j] == search ):
                isPresernt = True
                a = i
                b = j
                break

    if(isPresernt):
        print("Value is present \n", array[a][b])
    else:
        print("404, is not present")

arrayTwo = [
    [1,2,3],
    [4,7,9],
    [6,3,1]
]

print("Adding of two array is : ")
for i in range(3):
    row = ""
    for j in range(3):
        row += str(array[i][j]+ arrayTwo[i][j])+ " "
    print(row)

print("Subraction of two array is : ")

for i in range(3):
    row = ""
    for j in range(3):
        row += str(array[i][j] - arrayTwo[i][j])+" "
    print(row)

 