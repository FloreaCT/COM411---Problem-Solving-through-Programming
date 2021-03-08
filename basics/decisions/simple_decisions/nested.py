#BEEP is asking a question
print('What type of coverdoes the book have?')
book = input()
#Decide which kind of book to choose: hard or soft
if book == 'soft':
  print('Is the book perfect-bound?')
  #Decide if its a perfect or imprefect bound
  bound = input()
  if bound == 'yes':
   print(book, 'cover, perfect-bound books are very popular!')
  else:
   print(book, 'cover, imperfectly-bound books are not that popular!')
elif book == 'hard':
  print('Books with hard covers can be more expensive!')
#IF no book is selected
else:
  print('I dont know this type of books')


