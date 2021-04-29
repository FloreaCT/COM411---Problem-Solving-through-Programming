#Start of Program
print("The program has started")
print("Please enter a standard character: ")

character = input()

if len(character) == 1:
  print(ord(character))
else:
  print("Please enter only 1 character")

print("Program ended!")

