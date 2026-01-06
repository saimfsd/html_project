number = int(input("Enter a number : "))
array = []

for i in range(number):
    array.append(input("Enter a name: "))

for x in range(len(array)):
    for i in range(len(array)-1):
        a = array[i]
        b = array[i+1]
        if a > b:
            array[i] = b
            array[i+1] = a

print(array)
