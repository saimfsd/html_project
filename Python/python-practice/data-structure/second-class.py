# ***** swap value ***** 
# x = 10
# y = 20
 
# def swapValue(a,b):
#     temp = a
#     a = b
#     b = temp
#     print("x = ",x,"\ny = ",y)
# swapValue(x,y)
# print('x = ',x,'\ny = ',y)


# ******************
# a = 20
# b = 100
 
# def swap():
#     temp = a
#     a = b
#     b = temp
 
# print("a =", a)
# print("b =", b)
# swap()
# print("a =", a)
# print("b =", b)
 

#  ************

# def calculate():
#     num1 = int(input("Enter a number 1:"))
#     num2 = int(input("Enter a number 2:"))
#     op = input("Enter a operator")

#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/"
#         print(num1 / num2)
#     else:
#         print("Invalid operatoe")

# calculate()

# ******** make seprate function

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b 

def calculate():
    num1 = int(input("Enter a first number :"))
    num2 = int(input("Enter a second number :"))
    op = input("Enter a operator (+, -, *, /): ")

    result = None

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = sub(num1, num2)
    elif op == "*":
        result = multi(num1, num2)
    elif op == "/":
        result = div(num1, num2)
    else:
        print("Invalid operatoe")
        return

    print("Result:", result)

calculate()




 