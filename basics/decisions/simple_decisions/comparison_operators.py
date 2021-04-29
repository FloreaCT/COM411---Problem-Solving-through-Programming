#1st number to compare
print('Please enter first number')
firstnum = int(input())
#2nd number to compare
print('Please enter the second number')
secnum = int(input())

#Show the result
if firstnum > secnum:
  print('The second number is the smallest.')
elif firstnum < secnum:
  print('The first number is the smallest.')
else:
  print('The numbers are equal!')