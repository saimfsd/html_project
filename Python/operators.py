# Arthimatic Operator
a = 10 
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)



# Comparision Operator 

a = 10 
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)




#Assignment operator
a = 100
b = 20
c = a = b
print("The comparison of " + a + " = " + b + " is " + c)



# addition equal to

math = 100
science = 20
c = math + science
print("The comparison of", math, + science, "is", c)

# subtraction equal to
a = 1000
b = 200
c = a - b
print("The comparison of", a, "-=", b, "is", c)

# multiplication equal to
a = 100
b = 20
c = a * b
print("The comparison of", a, "*=", b, "is", c)

# division equal to
a = 100
b = 20
c = a / b
print("The comparison of", a, "/=", b, "is", c)

print("==========================================")



#Bitwise operator


a = 5   # binary: 0101
b = 3   # binary: 0011

print("a & b =", a & b)   # 1   (0001)
print("a | b =", a | b)   # 7   (0111)
print("a ^ b =", a ^ b)   # 6   (0110)
print("~a =", ~a)         # -6
print("a << 1 =", a << 1) # 10  (1010)
print("a >> 1 =", a >> 1) # 2   (0010)


#logical Operators 

a = 10
b = 5

# and operator
print(a > 5 and b < 10)         # True (both are True)
print(a > 15 and b < 10)        # False (first is False)

# or operator
print(a > 5 or b > 10)       # True (first is True)
print(a < 5 or b > 10)       # False (both False)

# not operator
print(not(a > b))            # False (a > b is True, not makes it False)