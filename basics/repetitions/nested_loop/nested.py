#Ask number of rows
print("How many rows should I have?")
rows = int(input())

#Ask number of columns
print("How many columns should I have?\n")
columns = int(input())

print("Here we go:\n")

emoji = ":)"
for x in range(0,rows,1):
  for x in range(0,columns,1):
    print(emoji,end="")
  print()