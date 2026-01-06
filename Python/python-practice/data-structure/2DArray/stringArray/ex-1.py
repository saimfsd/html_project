a = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

o = [
    ['j','k','l'],
    ['m','n','o'],
    ['p','q','r']
]

for i in range(len(a)):
    box = ""
    for j in range(len(o)):
        box += a[i][0] + o[0][j] + " + " + a[i][1] + o[1][j] + " + " + a[i][2] + o[2][j] + "  "
    print(box)

    A=[['a','b','c'],
   ['d','e','f'],
   ['g','h','i']]
 
B=[['j','k','l'],
   ['m','n','o'],
   ['p','q','r']]
 
for i in range(len(A)):
    box = ""
    for j in range(len(B)):
        box += (
            A[i][0] + B[0][j] + " + " +
            A[i][1] + B[1][j] + " + " +
            A[i][2] + B[2][j] + "   "
        )
    print(box)