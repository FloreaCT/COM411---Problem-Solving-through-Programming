#Start of the program
print('''It seems that i've lost my batery. Where should i look for it?
1. Living room
2. Bathroom
3. Bedroom
4. Kitchen
''')

#Decide where to look for the battery.
place = input().lower()

if place in ['living room', '1']:
  print('I am now looking in the the living room.')
  print('''Where in the living room should i look?
  1. Behind the TV.
  2. Under the couch.
  3. Behind the curtains.
  4. Under the dog
  ''')

  livingroom = input().lower()

  if livingroom in ['behind the tv', '1']:
    print('I am looking behind the TV.')
    print('I have found a video game but not the battery.')

  elif livingroom in ['under the couch', '2']:
    print('I am looking under the coach.')
    print('Found a lot of dust but no battery.')  

  elif livingroom in ['behind the curtains', '3']:
      print('I am looking behind the curtains.')
      print('I found some cats but no battery.')

  elif livingroom in ['under the dog', '4']:
    print('I am approaching the dog.')
    print('Woof, woof.')
    print('The dog seems to be angry at you for disturbing him. The dog left and ......')
    print('BEEP: You didnt really think it was there, where you?')
    print('BEEP: Your judgment seems to be unreliable so im going to search it on my own. Searching, searching ..... Found my battery!')

  else:
   print('BEEP is Going out of the room.')

elif place in ['bathroom', '2']:
  print('''Where in the bathroom should i look?
  1. Cupboard.
  2. Bathtub.
  3. Toilet.
  ''')

  look = input().lower()

  if look in ['cupboard', '1']:
    print('I am looking inside the Cuboard.')
    print('I found some towels but no battery.')

  elif look in ['bathtub', '2']:
    print('I am looking in the bathtub.')
    print('Found my battery!')

  elif look in ['toilet', '3']:
    print('I am not gonna look there!')

  else:
    print('BEEP is going out of the bathrom')

elif place in ['bedroom', '3']:
  print ('''Where in the bedroom should i look?
  1. Under the duve.
  2. Under the bed.
  3. Under the cat.
  ''')

  under = input().lower()

  if under in ['under the duve', '1']:
    print('Looking under the duve.')
    print('Found the dog but no battery.')

  elif under in ['under the bed', '2']:
    print('Looking under the bed.')
    print('Found the dog but no battery.')

  elif under in ['under the cat', '3']:
    print('''Approaching carefully the cat.
The cat seems to be asleep.
I'm removing the cat.
You didnt really think it was there, did you?
Your judgment seems to be unreliable so im going to search it on my own. Searching, searching ..... Found my battery! 
''')

  else:
    print('BEEP is going out of the bedroom.')

elif place in ['kitchen', '4']:
  print('''Where in kitchen should i look?
1. In the fridge.
2. Under the sink.
3. Under the table.
  ''')

  kitchen = input().lower()

  if kitchen in ['in the fridge', '1']:
    print('Isnt it wierd that you want me to look here?')
    print('Found some food but no battery.')

  elif kitchen in ['under the sink', '2']:
    print('I am looking under the sink.')
    print('Found some broken pipes but no battery. Should i repair the pipes? Yes/No')
    pipes = input()

    if pipes in ['yes', 'Yes']:
      print('Repairing the pipes.')
      print('Still no battery found.')

    else:
      print('Still no battery.')

  elif kitchen in ['under the table', '3']:
    print('I am looking under the table.')
    print('I found my baterry!')

  else:
    print('I will go search for the battery on my own.')

else:
  print('Guess i will never find the battery :(.')