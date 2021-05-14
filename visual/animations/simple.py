import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r


fig, ax = plt.subplots()
line, = ax.plot([], [], "ro-")

def animate(frame):
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  line.set_data(range(frame), range(frame))
  # colours = ["r","g","b"]
  # point = "o" + colours[r.randint(0,2)]
  # ax.plot(frame, frame, point)
  return line
def run():
  some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)
  plt.show()


run()

