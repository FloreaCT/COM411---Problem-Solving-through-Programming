word=input("What is the word ?\n")
print ("Reversing")
for position in range (len(word) -2, -2, -1): #WHY?!
  print(word[position], end="")