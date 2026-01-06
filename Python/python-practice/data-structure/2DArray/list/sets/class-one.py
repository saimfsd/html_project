#it does not Support the indexing 
#it underered collection of items 
#it does not support duplicate values


number = {1 ,2 ,3 ,4 ,5 ,6 }
print(number)

fruits ={"Apple ", "Banana" , "Cherry ", "apple"}
print(fruits)

fruits ={"Apple ", "Banana" , "Cherry ", "apple"}
for i in range(3):
    print(fruits)
#CONVERTED INTO TOUPLE

 fruitList = fruits.tuple(fruits)
print(fruitList)


#Function in sets
fruits.add("Mango")
print(fruits)


fruits.update(["Orange","Kiwi"])
print(fruits)


fruits.remove("Orange")
print(fruits)

#thw values add in last
fruits.discard("Apple")
print(fruits)


#HAsh function 
x = "hello"
print(hash(x))

#give the unique value 

#range remove the element using pop 



for i in range(4):
    fruits.pop()

print(fruits)

