# Ask user about the type of book

print("What type of book is this?")
book = input().lower()
if book == 'adventure':
    print("I like adventure books!")
elif book == 'Sci-Fi':
    print('I like Sci-Fi books!')
else:
    print('I dont recognize that book')

print('Finished reading book')
