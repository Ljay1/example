import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
from matplotlib.ticker import NullFormatter, FixedLocator

df = pd.read_excel('./Data/2106040301_175911#128379.xlsx')

# V-D-C view - Data - Controller
#Object 는 객체를 만들어 주게하는 객체
# print(df["Cond Inlet Pressure"])

find_index = []

for index, x in enumerate(list(df.loc[0])):
  if (x == "MPa"):
    find_index.append(index)
    
print(find_index)
# df.loc[(df["Cond Inlet Pressure"] & df["MPa"])]

# print(df["Cond Inlet Pressure"].isin(["MPa"]))

# print(df == "MPa")

# print(set(df.loc[0]))

# list_of_channels= 

# print(df.head(1))
# head_list = list(df.head(1))

# print(df.columns[find_index]) ## 채널 이름 filter

# print(df[list_of_channels])

list_of_channels = df.columns[find_index]
df1= df[list_of_channels]
df2=df1.drop(0)


df2.plot()

# ax.set_yscale('function', functions=(forward, inverse))
# ax.set_title('function: Mercator')
# ax.grid(True)
# ax.set_xlim([0, 180])
# ax.yaxis.set_minor_formatter(NullFormatter())
# ax.yaxis.set_major_locator(FixedLocator(np.arange(0, 90, 10)))

# plt.show()

plt.xlim(0, 150)
# X축 & Y축 Label 설정
plt.xlabel('Time', fontsize=10)
plt.ylabel('Press.', fontsize=10)

# X tick, Y tick 설정
plt.xticks(rotation=0)
plt.yticks(rotation=30)

# 타이틀 & font 설정
plt.title('P-T Diagram', fontsize=20)

plt.show()