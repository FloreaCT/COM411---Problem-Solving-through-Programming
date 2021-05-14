import matplotlib.pyplot as plt

def display(x_values,y_values):
  plt.plot(x_values, y_values)

  plt.xlabel("X Value")
  plt.ylabel("Y Value")

  plt.show()

def run():
  x = [1,2,3,4,5]
  y = [1,4,9,16,25]
  display(x,y)


run()

