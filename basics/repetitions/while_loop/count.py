#Display the question
print('How many live cables should i remove?')

#Capture user input
live_cables = int(input())

#Set variable to 0
alive_cables = 0


#Print the number of avoided cables. 
#!!! In the exercise it is being asked to use end='' in order to stay on the same line. I dont understand the needing of using that kind of command in this situation as per the example under.
while ( alive_cables < live_cables):
  print('Avoiding..Done!',alive_cables +1, 'live cables avoided. ')
  alive_cables = alive_cables + 1 

#I see now, since the counting starts from 0 and we dont want to print 0 cables avoided, we first print half of the sentence, and then we increase the number of the variable, and then we continue to print on the same line with end='' after the variable has been increased. Is the way i did it wrong? One less print command to be compiled x the loop number.

# while (cables_avoided < cables_to_avoid):
#     print("Avoiding...", end="")
#     cables_avoided = cables_avoided + 1
#     print("Done!", cables_avoided, "cables avoided.")

print('')
print('All live cables have been avoided!')