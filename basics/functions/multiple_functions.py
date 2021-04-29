#Defining the function
def display_ladder(steps):
  print()
  print("| |\n***\n" * steps)

def create_ladder():
  print("How many steps are left?")
  steps = int(input())
  display_ladder(steps)

create_ladder()