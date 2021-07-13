import numpy as np
import pandas as pd

df = pd.read_excel('./Data/2106040301_175911#128379.xlsx')

# V-D-C view - Data - Controller
#Object 는 객체를 만들어 주게하는 객체
# print(df["Cond Inlet Pressure"])

# df.loc[(df["Cond Inlet Pressure"] & df["MPa"])]

# print(df["Cond Inlet Pressure"].isin(["MPa"]))

# print(df == "MPa")

# print(list(df.loc[0]))
find_index = []

for index, x in enumerate(list(df.loc[0])):
  if (x == "MPa"):
    find_index.append(index)
    
print(find_index)

# print(df.head(1))
# head_list = list(df.head(1))

# print(df.columns[find_index]) ## 채널 이름 filter

list_of_channels = df.columns[find_index]

print(df[list_of_channels])