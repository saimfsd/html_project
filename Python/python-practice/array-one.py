array = []

print(array)
a = 10
b = 20
c = 30

# use for insert single value
# array.append(a)
# array.append(a)
# array.append(a)
# array.append(a)
# print(array)

# use for inserting multipal valu
array.extend([a,b,c])
print(array)

# insert value in any index number (arg1 = index no, arg2 = value for insert )
array.insert(3,2)
print(array)

# use to clear array
array.clear()
print(array)


# marge two array 
array = [9,8,7,6]
newArray = [5,4,3,2]

array.extend(newArray)
print(array)


# removing value from array using index or by default it remove last index value (pop get only one argument)
array.pop(2)
print(array)

cars = ["BMW", "HONDA", "SUZUKI", "VOLVO"]
print(cars)

cars.remove("HONDA")
print(cars)

# print table 
table = []
for i in range(1,11):
  table.append(i * 2)
print(table)



for i in range(3):
  number = int(input("Enter a value :"))
  table.append(number)

print(table)


