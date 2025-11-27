num = int(input("Enter a value: "))
array = []
i = 0

while i < num:
    array.append(i+1)
    i = i + 1   # important

print(array)


# Second 
#array = []
#for i in range(1, 100):
  #  if i % 3 == 0:
     #   array.append(i)
    #elif i % 7 == 0:
      #  array.append(i)

print(array)

#third 
for i in range(1, 50):
    if i % 2 == 0:
        print("The number is even " + str(i))
    else:
        print(i)

        