import matplotlib.pyplot as plt

def small():
  plt.plot([3,3,4,4,3], [3,4,4,3,3], "ro:")


def medium():
  plt.plot([2,2,5,5,2], [2,5,5,2,2], "gs--")


def large():
  plt.plot([1,1,6,6,1], [1,6,6,1,1], "bp-")
  
  small()
  medium()
  plt.show()
large()



