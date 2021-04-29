#Get user input
print("How far are we from the cave?")
distance = int(input())

for x in range(distance, 0, -1):
  print(x, "steps remaining")

print("We have reached the cave!")