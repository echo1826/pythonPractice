# Write a function that determines if a number is even or not

# First iteration
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# One-liner solution
def is_even(num):
    return num % 2

print(is_even(4))
print(is_even(5))

# Write a function that takes a phrase and replaces the spaces with dashes
def slugify(phrase):
    return phrase.strip().replace(" ", "-").lower()
print(slugify("Turn this into a url slug"))

# Write a function that takes a string and counts the vowels in the string
def vowel_count(phrase):
    count = 0
    for char in phrase:
        if char in 'aeiou':
            count += 1
    return count
print(vowel_count("hello world"))