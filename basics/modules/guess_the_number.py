import random as rnd
def play_guess_the_number():
  #Set minimum value
  print("Please enter the minimum value: ")
  minimum = int(input())
  
  #Set maximum value
  print("Please enter the maximum value: ")
  maximum = int(input())

  random_number = rnd.randrange(minimum,maximum)

  print(f"I am thinking of a number between {minimum} and {maximum}. Can you guess what it is?")

  guess = int(input())
  while True:
    if guess < random_number:
      print("Your guess is too low.")
      print("Try again")
      guess = int(input())
    elif guess > random_number:
      print("Your guess is too high.")
      print("Try again")
      guess = int(input())
    elif guess == random_number:
      print( "Congratulations! You guessed my number!")
      return guess

play_guess_the_number()

