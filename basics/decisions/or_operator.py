#Ask for the path to take
print("What type of adventure should i have?")
adventure = input()

#Identify the type of path
if (( adventure == 'short') or (adventure =='scary') or (adventure ==' dangerous')):
  print('Entering the dark forest!')
elif ((adventure == 'long') or (adventure == 'safer')):
  print('Taking the safer route!')
else:
  print('Teleporting to the moon and back .... Then we will pick another route? Either the short one or the long one.')