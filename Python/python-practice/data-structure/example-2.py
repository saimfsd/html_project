sum = 0
avg = 0

i = 0
while(i<3):
    num = input("Enter a number : ")
    if(num >= ':' and num <= '~'):
        print("Invalid input, please enter number")
    else:
        sum += int(num)
    i = i+1

avg = sum / 3
print(avg)



