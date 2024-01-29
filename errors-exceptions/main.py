# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# dictionary = {"key": "value"}
# value = dictionary["non_existent_key"]

# Pattern for catching exceptions
# try: -> code that might cause an exception
# except: -> if there was an exception (error) run the error handler
# else: -> if there was no exceptions raised, run this code
# finally: -> this code will run no matter if there was an exception raised or not

try:
    file = open("a_file.txt")
    # dictionary = {"key" : "value"}
    # print(dictionary["sdfsdf"])
# this bare except clause will run on any error, rather than a specific error
# except:
except FileNotFoundError: # this exception will run only on a FileNotFoundError
    file = open("a_file.txt", "w") # create the file we're trying to open if it doesn't exist
    file.write("Something")
    print("file created")
# can chain on multiple except clauses that runs for specific errors
except KeyError as error: # how to grab the error message in an exception
    print("That key does not exist.")
    print(error)
else: 
    content = file.read()
    print(content)