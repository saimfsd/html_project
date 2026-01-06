announcements = [
    ["Train delayed", "Platform change"],
    ["Train arriving"],
    ["Train cancelled", "Maintainence work"]
]
 
 
# Replace "Train" with "Express"

announcements = [
    ["Train delayed", "Platform change"],
    ["Train arriving"],
    ["Train cancelled", "Maintainence work"]
]

# Print announcement platform-wise
for i in range(len(announcements)):
    print("Platform", i + 1, announcements[i])
     
    print("------------------------------")

# Search "cancelled" (case-insensitive)




# Count total announcements
count = 0
for i in range(len(announcements)):
       count += len(announcements[i])

print("Total announcement :", count)

print("------------------------------")

 

# Replace "Train" with "Express"



for i in range(len(announcements)):
    for j in range(len(announcements[i])):
        announcements[i][j] = announcements[i][j].replace("Train", "Express")

print("Updated announcements:")
print(announcements)



 

