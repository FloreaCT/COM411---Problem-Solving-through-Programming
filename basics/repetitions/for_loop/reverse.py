#Ask the user for a sentence
print("What phrase do you see?\n")
phare = input()

print("\nReversing...")
print("The phrase is:\n")
#Reverse the sentence
for x in range(len(phare) - 1, -1, -1):
    print(phare[x], end="")
