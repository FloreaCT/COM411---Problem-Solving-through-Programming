class Human: #This is the class name

  MAX_ENERGY = 100 # This is the class attribute

  def __init__(self): #This is the initializer

    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY


  def display(self):
     print(f"I am {self.name}")

  def __repr__(self):
  return f'human(name={self.name}, age={self.age})'

  def __str__(self):
    return f'Human {self.name} is {self.age} years old.'

if (__name__ == "__main__"):

  human = Human()
  human.display()

