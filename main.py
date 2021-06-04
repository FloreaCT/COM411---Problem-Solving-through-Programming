from oop.human import *
from oop.robot import *

if (__name__ == "__main__"):

  human = Human()
  human.display()

def __repr__(self):
  return f'robot(name={self.name}, age={self.age})'

def __str__(self):
  return f'Robot {self.name} is {self.age} years old.'

print(repr(obj))


# class Robot:

#   # A class attribute
#   laws = "Protect, Obey and Survive"

#   # A static method
#   @staticmethod
#   def the_laws():
#     print(Robot.laws)

#   # a class method
#   @classmethod
#   def assemble(cls):
#     return cls("Assembled Robot")

#   # An initialiser (special instance method)
#   def __init__(self, name = "Robot"):

#     # An instance attribute
#     self.name = name
#     self.age = 0

#   # An instance method
#   def display(self):
#     print(f"I am {self.name}")
  

# R1 = Robot()
# R2 = Robot("Beep")
# R3 = Robot.assemble()

# R1.display()
# R2.display()
# R3.display()