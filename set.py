webdev = {'SQL', 'css', 'html', 'js', 'python'}

data = {'R', 'SQL', 'python'}

# print(type(webdev), data)

# intersection of sets (anything that is in both sets)
common_tech = webdev & data
# another way of doing intersection
common_tech_method = webdev.intersection(data)
print(common_tech)

# union of sets (all items from both sets, if there are duplicates only lists it once)
everything = webdev | data
# another way of doing union
everything_method = webdev.union(data)
print(everything)

# difference of sets (returns new set with members from left that doesn't exist in the right set)
no_common = webdev - data
# another way of doing difference
no_common_method = webdev.difference(data)
print(no_common)

# why to use sets?
# sets make it very east/fast to check if a value exists in a collection
# if checking a value exists in an array it's a lot faster to use a set rather than an array (big O notation stuff)
# sets are an easy way to remove duplicates from a collection