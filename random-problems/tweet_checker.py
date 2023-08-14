tweet = input("Enter your tweet: ")

if len(tweet) < 140:
    print(f"That {len(tweet)} character tweet will work!")
else:
    difference = len(tweet) - 140
    print(f"Your {len(tweet)} character tweet is {difference} characters too long")