# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# My solution
# wrong_input = True
# while(wrong_input):
#   try: 
#     word = input("Enter a word: ").upper()
#     if not word.isalpha():
#       raise KeyError
#   except KeyError:
#     print("Sorry, only letters in the alphabet can be inputted.")
#   else:
#     wrong_input = False

# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)


# Course Solution
def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
  except KeyError: 
    print("Sorry, only letters in the alphabet can be inputted.")
    generate_phonetic()
  else:
    print(output_list)
    
generate_phonetic()