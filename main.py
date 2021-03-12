#Display the question
print('How many live cables should i remove?')

#Capture user input
live_cables = int(input())

#Set variable to 0
alive_cables = 0

#Print the number of avoided cables. 
#!!! In the exercise its being asked to use end='' in order to stay on the same line. I dont understand the needing of using that kind of command in this situation as per the example under.
while ( alive_cables < live_cables):
  print('Avoiding..Done!',alive_cables +1, 'live cables avoided. ')
  alive_cables = alive_cables + 1

print('')
print('All live cables have been avoided!')