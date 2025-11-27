userinput = int(input("Enter a number: "))
fact = 1
a = ""  # Ye string me multiplication sequence store karega

for i in range(userinput, 0, -1):  # userinput se 1 tak reverse
    fact *= i                     # factorial calculate
    a += str(i)                   # string me i add karenge
    if i != 1:
        a += "*"                  # 1 se pehle * add karenge

print(f"{a} = {fact}")
