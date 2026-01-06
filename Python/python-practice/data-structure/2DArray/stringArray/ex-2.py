# print Student List class-wise
# Count total Student
# check if Ayush is present or not
# Convert all names to uppercase

studentList = [
    ["Pranamya", "Ashish", "Ayush"],
    ["Vaishali", "Divya"],
    ["Minal", "Sama", "Alfiya", "Rutuja"]
]
 
# print student list class-wise
for i in range(len(studentList)):
    print("Class", i+1, "students:")
    for j in range(len(studentList[i])):
        print(studentList[i][j])
    print()   
 
# count total student
total = 0
 
for i in range(len(studentList)):
    total += len(studentList[i])
print("Total students =", total)
 
# check if Ayush is present or not
if "Ayush" in studentList[0]:
    print("Ayush is present")
else:
    print("Ayush is not present")
 
# convert all name to uppercase
for i in range(3):
    for j in range(len(studentList[i])):
        studentList[i][j] = studentList[i][j].upper()
 
print(studentList)
 

# convert all student names to uppercase
for i in range(len(studentList)):
    for j in range(len(studentList[i])):
        studentList[i][j] = studentList[i][j].upper()

print(studentList)