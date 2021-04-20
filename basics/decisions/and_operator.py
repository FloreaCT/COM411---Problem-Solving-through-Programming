print('What did i hear?')
hear = input()
print('What did i see?')
see = input()
if (hear == 'hoot') and (see == 'some big eyes'):
  print('I am a little scared but I will continue!')
#Just interconnecting "or" and "and"
elif (((hear == 'hoot') or (hear == 'scary')) and ((see == 'yes') or (see == 'no')) or (hear == 'scary')):
  print('SCAAAAAAAAAAAAAARY')
else:
  if (hear == 'grrr') and (see == 'two red eyes'):
    print('There is a scary creature. I should get out of here!')