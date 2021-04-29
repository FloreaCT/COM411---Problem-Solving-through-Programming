#Start of Program
print("The program has started")
print("Please enter a standard character: ")
#Capture the user input
character = input()

#Convert character into ASCII 
if len(character) == 1:
  print(ord(character))
else:
  print("Please enter only 1 character")

print("Program ended!")

