#Defining 1st function
def sum_weight(beep,bop):
  total = beep + bop
  return total

#Defining 2nd function
def calc_avg_weight(beep, bop):
  average = int((beep + bop) / 2)
  return average

#Defining 3rd function
def run():
  #Ask user for weight values
  beep = int(input("Please enter the weight of Beep: "))
  bop = int(input("Please enter the weight of Bop: "))

  print("Please choose sum or average.")
  choose = input()
  #Calculate the sum or the average
  if choose == "sum":
    print("The sum of Beep and Bop is:", sum_weight(beep,bop))
  elif choose == "average":
    print("The average of Beep and Bop is:",calc_avg_weight(beep,bop))

run()