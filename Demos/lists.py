#Define an empty list
fruits = []

#Define a list with items

vegetables = ['Carrot', 'Peas']

#Add itemes to the list

fruits.append("Apple")
fruits.append('Banana')
fruits.append('Tomatoe')
fruits.append('Banana')

print(fruits)

#Remove an item from list
fruits.remove('Banana')

print(fruits)

#Remove item b index
del fruits[1]
print(fruits)

#Insert a value not at the end
fruits.insert(1, "Pineapple")
print(fruits)

#Access single element
print(fruits[0])


def get_fruits():
  fruits = []

  for i in range(4):
    print('Type in the next fruit:')
    fruits.append(input())
  print('Your fruits are {}'.format(fruits))

  print(f"Sliced list is: {fruits[0:5]}")
#  print(f"Sliced list is: {fruits[0:5:2]}) 0 is the start point which is included, 5 is the end point which is excluded and 2 is the steps

#Print only few items b using negative index
  print(f"Negative index: {fruits[-2:0:-1]}")

get_fruits()

#Ask the user how many fruits to enter 

def get_fruits():
  fruits = []
  print('How many fruits would you like to enter')
  n = int(input())
  for i in range(n):
    print('Type in the next fruit:')
    fruits.append(input())
  print('Your fruits are {}'.format(fruits))

get_fruits()