#Union 
#Intersection 
#Subset 
#Superset 

#Union 
A = {1, 2, 3, 4}
B = {3, 4}

print(A | B)
# Output not repeated 
#{1, 2, 3, 4, 5}

#Using functon 
A = {1, 2, 3}
B = {3, 4, 5}

result = A.union(B)
print(result)




#Intersection 

#Find repeat and print 

A = {10, 20, 30}
B = {30, 40, 50}

print(A & B)


#Using function 
A = {10, 20, 30}
B = {30, 40, 50}

result = A.intersection(B)
print(result)








#Subset 
#Small set is present in big set so give the values true aur false 

A = {1, 2, 3, 4}
B = {2, 3}

print(B.issubset(A))


#Superset 
A = {1, 2, 3, 4}
B = {2, 3}

print(A.issuperset(B))







