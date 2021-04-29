#Defining 1st function
def display_box(word):
  print("*" * len(word))
  print(word)
  print("*" * len(word))

def display_lower(word):
  print(word.lower())

def display_upper(word):

  print(word.upper())

def mirrored(word):
  print(word, "| " , end="")
  for x in range(len(word) -1, -1, -1):
    print(word[x],end="")

def repeat(word):
  print("How many times should I repeat the word?")
  repeat = int(input())
  upper = 0
  lower = 0

  for x in range(repeat):
    if x % 2 == 0:
      display_upper(word)
    else:
      display_lower(word)
  


def run():
  print("Please choose the word you would like to decrypt.")
  word = input()
  print()
  print("How should we decrypy the word?")
  print("1) Display in a Box – display the word in an ascii art box\n2) Display Lower-case – display the word in lower-case\n3) Display Upper-case – display the word in upper-case\n4) Display Mirrored – display the word with its mirrored word\n5) Repeat – ask the user how many times to display the word")
  dword = int(input())
  if dword == 1:
    display_box(word)
  elif dword == 2:
    display_lower(word)
  elif dword == 3:
    display_upper(word)
  elif dword == 4:
    mirrored(word)
  elif dword == 5:
    repeat(word)

run()
