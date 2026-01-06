rows = int(input("Enter a number of rows : "))
colums = int(input("Enter a number of columns : "))

array = []

for i in range(rows):
    a = []
    for j in range(colums):
        inputValue = int(input("Enter a value : "))
        a.append(inputValue)
    array.append(a)

for i in range(rows):
    row = ""
    for j in range(colums):
        row += str(array[i][j])+" "
    print(row)

    