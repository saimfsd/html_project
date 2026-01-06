Userinput = "nitin "
reverse = ""

for i in reversed(range(len(Userinput))):
    reverse += i

if Userinput == reverse:
    print("It is palindrome")
else:
    print("It is not palindrome")


#Second problem you have to solve this
 

word = "nitin"
reverse_word = ""

# Making reverse of the word
for i in range(len(word) - 1, -1, -1):
    reverse_word += word[i]

# Compare both
if word == reverse_word:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")