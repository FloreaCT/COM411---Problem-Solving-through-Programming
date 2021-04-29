<<<<<<< HEAD

def also(a,a):
  print(a)
  print(b)


x = ['Earth', TRUE, 9.8]
y = [0,1]


also(x,y)
=======
import json

def shop():
  with open("items.json") as json_file:
    items = json.load(json_file)
  return items

def save_items(items = {}):
  json_database = open("items.json", "w")
  json.dump(items, json_database, indent = 4)
  json_database.close()

def view_all(products = {}):
  for i in products:
    print(i)

def basket():
  basket = []
  while True:
    item = input("Enter item (or \"stop\"): ")
    if item == "stop":
      break
    else:
      basket.append(item)
  return basket

def till(basket = []):
  shoplist = shop()
  total = 0.0
  for item in basket:
    total += shoplist[item]
  return total

def run():
  print("Welcome to Pete's shop! Please have a look around and add items you like!")
  view_all(shop())
  chosen_items = basket()
  while True:
    print("Are you ready to pay?")
    if input().lower() == "yes":
      to_pay = till(chosen_items)
      print(f"Please pay {to_pay:.2f} by cash or card")
      break
    else:
      chosen_items += basket()

run()

>>>>>>> 4a950ac110b968f17033bbc2dea3c2dd5d07f386
