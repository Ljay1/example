import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests
import numpy as np

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

plt.rc('font', family='NanumGothic', size=10)
plt.rcParams["figure.figsize"] = (12, 9)

# url = "https://api.upbit.com/v1/market/all"

# querystring = {"isDetails":"false"}

# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"

def getPrice():

  headers = {"Accept": "application/json"}

  response = requests.request("GET", url, headers=headers)

  # print(response.text)

  res = response.json()
  # print(res)

  data = res[0]
 
  # print(data["trade_price"])
  return data["trade_price"]

frame_len = 20
y = []
def animate(i):
  y.append(getPrice())
  
  if len(y) <= frame_len:
    plt.cla() # clear plot
    plt.plot(y, 'r', label = '가격 (원)')
  else:
    plt.cla() # clear plot
    plt.plot(y[-frame_len:], 'c', label = '가격 (원)')

  # plt.yticks(np.arange(38400000, 39000000, 50000))
  plt.ticklabel_format(axis='y', style='sci', useMathText=True)

  plt.xlabel('Time (s)')
  plt.ylabel('가격 (원)')
  plt.legend(loc = 'upper right')
  plt.grid()
  
  plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.show()