#Defining the function
def greet_user():
  #Ask for the name
  print('What is your name stranger?')
  name = input()

  #Greet the user
  print('Pleased to meet you',name,'.''\n')

  #Ask for the reason
  print('Are you here to help BEEP?')
  help_beep = input()
  if help_beep in ['Yes', 'yes']:
    print('Im so happy BEEP has friends like you.')
  else:
    print('You should be on your way',name,'.')
  

greet_user()

