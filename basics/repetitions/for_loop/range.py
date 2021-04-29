#Ask user for the brightness level
print("What level of brightness is required?")
brightness = int(input())

print("Adjusting brightness...")

#Adjust the level of brighness
for x in range(2, brightness + 1, 2):
  print("Beep's brightness level:", "*" * x)
  print("Bop's brightness level:", "*" * x, "\n")

print("Adjustment complete!")
