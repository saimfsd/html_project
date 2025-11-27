# str1 = input("Enter a sentence: ")
# aCount = 0
# iCount = 0
# eCount = 0
# oCount = 0
# uCount = 0
# consonantCount = 0

# for i in range(len(str1)):

#     if str1[i] == 'a' or str1[i] == 'A':
#         aCount += 1
    
#     elif str1[i] == 'i' or str1[i] == 'I':
#         iCount += 1

#     elif str1[i] == 'e' or str1[i] == 'E':
#         eCount += 1

#     elif str1[i] == 'o' or str1[i] == 'O':
#         oCount += 1

#     elif str1[i] == 'u' or str1[i] == 'U':
#         uCount += 1

#     else :
#         consonantCount += 1


# print("a :", aCount)
# print("i :", iCount)
# print("e :", eCount)
# print("o :", oCount)
# print("u :", uCount)
# print("Consonants :", consonantCount)

name = input("Enter your name: ")
count = 0

for i in range(len(name) - 1):

    if (
     
        (name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u' or
         name[i] == 'A' or name[i] == 'E' or name[i] == 'I' or name[i] == 'O' or name[i] == 'U')

        and

        # second vowel check
        (name[i+1] == 'a' or name[i+1] == 'e' or name[i+1] == 'i' or name[i+1] == 'o' or name[i+1] == 'u' or
         name[i+1] == 'A' or name[i+1] == 'E' or name[i+1] == 'I' or name[i+1] == 'O' or name[i+1] == 'U')
    ):
        count += 1

print("Total vowel pairs =", count)



