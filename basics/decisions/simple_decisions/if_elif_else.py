#Ask user for the desired direction to paint
print('Towards which directions should I paint (up, down, left, right)?')
direction = input().lower()

if direction == 'up':
  print('I am painting in the upward direction!')
elif direction == 'down':
  print('I am painting in the downward direction!')
elif direction == 'right':
  print('I am painting in the right direction!')
elif direction == 'left':
  print('I am painting in the left direction!')
else:
  print('Direction unknown, please input the correct direction (up, down, left or right)')
