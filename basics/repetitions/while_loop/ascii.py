#Display the question
print('How many bars should be charged?')

#Caputre user input.
bar = int(input())

#Define the variables
bars = 0

#Life bar code
while (bars < bar):

  print('Charging: ', end='')
  
  bars = bars + 1
  health = '\u2588 ' * bars

  print(health)

#Display the health bar
print('\n''The battery is fully charged.')