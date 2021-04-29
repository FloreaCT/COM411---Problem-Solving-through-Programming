#Display the question
print('How many live cables should i remove?')

#Capture user input
live_cables = int(input())

#Set variable to 0
alive_cables = 0


#Print the number of avoided cables. 

while (alive_cables < live_cables):
  print('Avoiding..Done!',alive_cables +1, 'live cables avoided. ')
  alive_cables = alive_cables + 1 


# while (cables_avoided < cables_to_avoid):
#     print("Avoiding...", end="")
#     cables_avoided = cables_avoided + 1
#     print("Done!", cables_avoided, "cables avoided.")

print('')
print('All live cables have been avoided!')