import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent

frame_len = 200
y = []
def animate(i):
  y.append(cpu_percent())
  
  if len(y) <= frame_len:
    plt.cla() # clear plot
    plt.plot(y, 'r', label = 'Real-Time CPU Usage')
  else:
    plt.cla() # clear plot
    plt.plot(y[-frame_len:], 'c', label = 'Real-Time CPU Usage')
    
  plt.ylim(0, 100)
  plt.xlabel('Time (s)')
  plt.ylabel('CPU Usage (%)')
  plt.legend(loc = 'upper right')
    
  plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.show()