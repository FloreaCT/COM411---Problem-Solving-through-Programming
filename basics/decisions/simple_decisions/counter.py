print('Please enter the first whole number')
firstnum = int(input())
print('Please enter the second whole number')
secnum = int(input())
print('Please enter the third whole number')
thirdnum = int(input())

#TIP: You can add variables within varibles to shorten the code i belive or to make it easier to read/write?
numbers = (firstnum, secnum, thirdnum) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers: #Defining where to find "X"
        if not x % 2: #Defining the statement
    	     count_even+=1 
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
print('')
print('Or it can be inputed as:') #Or it can be inputed as:
print('')

#Also ask for a better explanation of what is happening here!

count_odd = 0
count_even = 0
for x in firstnum, secnum, thirdnum:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("There were {} even and {} odd numbers.".format(count_even, count_odd))
print("\n")
#
print("""And in the solution we have: \n

if (firstnum % 2 == 0):
    firstnum = firstnum + 1
else:
    firstnum = firstnum + 1

if (secnum % 2 == 0):
    secnum = secnum + 1
else:
    secnum = secnum + 1

if (thirdnum % 2 == 0):
    thirdnum = thirdnum + 1
else:
    thirdnum = thirdnum + 1
 """)