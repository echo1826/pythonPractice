# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input([{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]))

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    # continue # continue will force the loop to end and start at the next iteration
    pass # pass will make sure the current iteration continues on and execute any code below


print(total_likes)