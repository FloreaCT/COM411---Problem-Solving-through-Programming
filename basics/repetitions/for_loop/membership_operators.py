# Ask the user for phrase
print("What phrase do you see?")
phrase = input()

# Print the reversed list
print("\nReversing...\nThe phrase is:\n", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed) 
  