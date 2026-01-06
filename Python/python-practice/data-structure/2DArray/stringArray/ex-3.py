experiments = [
    ["acid test", "salt test"],
    ["flame test"],
    ["ph test", "iodine test"]
]

# count total experiments
 
 
# find the day with maximum experiments
 
count = 0
for i in range(len(experiments)):
    count += len(experiments[i])

print("Total Experiments: ", count)
print("---------------------------")

# print only experiments containing the word "test"
for i in range(len(experiments)):
    for j in range(len(experiments[i])):
        if("test" == experiments[i][j]):
            print(experiments[i][j])

# convert all experiment name to the "Title Case"
result = []
for i in range(len(experiments)):
    temp = []
    for j in range(len(experiments[i])):
        titleWords = experiments[i][j].split(" ")
        a = []
        for k in range(len(titleWords)):
            titleWords.append(k[0].upper()+k[1])
        temp.append(" ".join(titleWords))
    result.append(temp)
print(result)
