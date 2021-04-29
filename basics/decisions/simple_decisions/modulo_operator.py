#Ask for the number to check 
print('Please enter a whole number')
number = int(input())

if (number % 2) == 0:
  #Using {} to print the statement
   print("{} is Even".format(number))
   
else:
  #Using the statement directly
   print(number, "is Odd.")