from random import randint



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

# dictionary comprehension
students_scores = {name: randint(1, 100) for name in names}
print(students_scores)

passed_students = {name: score for (name, score) in students_scores.items() if score >= 60}
print(passed_students)

# you can loop through a dataframe a lot like how you loop through a dictionary
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# Loop through dataframe without built-in methods
# for (key, value) in student_data_frame.items():
#     print(key)

# Loop through dataframe with built-in pandas methods
for (index, row) in student_data_frame.iterrows():
    print(row.score)