count = 0
word = raw_input("Please enter a phrase: ")
for letter in word:
    if letter in "aeiou":
        count +=1
print "Number of vowels: ", count
