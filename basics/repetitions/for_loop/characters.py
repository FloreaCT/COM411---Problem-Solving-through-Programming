#Ask user for some characters
print("What strange markings do you see?")
characters = input()

print("Identifying...")

for x in range(len(characters)):
  print("index 0:", characters[x])

print("Done!")