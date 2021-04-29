#Start the program
print("How many numbers should I sum up?")
numbers = int(input())

#Define the variables
counter = 1
total = 0

#Start the calculations
while (counter < numbers + 1):
  print("Please enter number", counter ,"of", numbers)
  total += int(input())
  counter += 1

#Show the answer
print("The answer is",total,".")