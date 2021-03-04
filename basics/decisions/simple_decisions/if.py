#First if statement. Ask user about the book
print("What type of book is this?")
book = input()
if book == 'adventure':
    print("I like adventure books!").lower()
elif book == 'Sci - Fi':
    print('I like Sci-Fi books!').lower()
else:
    print('I dont recognize that book')
print('Finished reading book')
