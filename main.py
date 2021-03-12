# The is function with single plan and name is plan

def escape_by(plan):
  if (plan == 'jumping over'):
    print('We cannot escape that way, the boulder is too big.')
  elif(plan == 'running around'):
    print('We cannot escape that way, the boulder is too fast')
  elif(plan == 'going deeper'):
    print('That might be a good idea, lets do it!')
  else:
    print('I am not sure what is the plan...')

escape_by('jumping over')
escape_by('running around')
escape_by('going deeper')
escape_by('no plan')