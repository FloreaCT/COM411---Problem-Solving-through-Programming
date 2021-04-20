phonebook = {}

while True:
  name = input('Enter the name: ')
  number = input('Enter the number: ')
  phonebook[name] = number
  if input('Type x to stop: ') == 'x':
    break

def calling(l, something = {}):
  print(f'Calling {l} with a phone number {something[l]}')

calling('Piotr', phonebook)
