numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Ethan"
# like a .split("") in JS
name_list = [char for char in name]
print(name_list)

# list comprehension can work for any sequence in python, not just lists
range_doubled = [num * 2 for num in range(1, 5)]
print(range_doubled)

# conditional list comprehension
# like a .filter()
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)