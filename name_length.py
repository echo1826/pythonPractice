first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("*" * 20)
average_length = 12
length_inputted = len(first_name+last_name)
if average_length > length_inputted:
    print(f"{first_name} {last_name} is shorter than the average American name")
elif average_length == length_inputted:
    print(f"{first_name} {last_name} is the same length as the average American name")
else:
    print(f"{first_name} {last_name} is longer than the average American name")

print("*" * 20)