
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)
print("*"*50)
# Write a while loop that does the same thing!
count = 0
while count < len(word):
    print(word[count])
    count += 1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
index = 100
while index <= 140:
    print(index)
    index += 2


# Write a for loop that does the same thing (with range())
for num in range(100, 141, 2):
    print(num)


#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

sillygoose_while = ""
while sillygoose_while != "sillygoose":
    sillygoose_while = input("Please type in sillygoose: ")

