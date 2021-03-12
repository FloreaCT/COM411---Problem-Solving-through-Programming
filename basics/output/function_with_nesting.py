#The function
def identify():
#Ask for the question
  print('What lies before us?')
  response = input()
#Check and display the message
  if (response == 'a large boulder'):
    print("It's time to run!")
    print('How fast BEEP and BOP should run?')
    run = input()
    if (run== 'fast','very fast','like crazy'):
      print('Beep and BOP are running', run)
    else:
      print('BEEP and BOP are running slowly.')
  else:
    print('We will be fine.')
#Call the function
identify()