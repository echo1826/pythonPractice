from textblob import TextBlob
# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello Employee Number 123510905960124. We hope you had a great day of work. It's time to submit your employee wellness statement")
# engine.runAndWait()

print("Enter your wellness statement: ")
phrase = input("> ")

blob = TextBlob(phrase)

while blob.sentiment.polarity < 0.5:
    print("More positive please: ")
    phrase = input("> ")
    blob = TextBlob(phrase)

print("We appreciate you too!")