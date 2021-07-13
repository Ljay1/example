# libaray install method
# pip install matplotlib
# version 설명 a.b.c  a= Major (함수 삭제) b= Minor (함수변경 시) , c= 에러/버그 수정 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./data/house_price_clean.csv')



# print (plt.rcParams['font.size'] ) 
# print (plt.rcParams['font.family'] )

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf') # ttf 일반적인 폰트 확장자
# print(font_list)

#print([(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name])
# print(mpl.get_cachedir()) cache 파일 찾기

# SETTINGS
plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams["font.size"] = 14
plt.rcParams["figure.figsize"] = (9, 6)


print(df)

df.plot()
plt.show()

# # # #data 실행
# # # data= np.arange(1,100)

# # # ## plot, 기본은 선 그래프
# # # plt.plot(data)
# # # plt.show()

# # # 다중 그래프
# # data= np.arange(1,53)
# # data2= np.arange(51,100)

# # plt.plot(data)
# # plt.plot(data2)
# # # plt.show()
# # plt.figure() # figure를 나눠서 새로운 그래프 그리고 싶을 때
# # plt.plot(data2 +50)
# # plt.show()

# # #Subplot (row, column, index)
# # data= np.arange(100,201)
# # plt.subplot(2,1,1)
# # plt.plot(data)



# # data2=np.arange(200,300)
# # plt.subplot(2,1,2)
# # plt.plot(data2)

# # plt.show()

# # data 생성
# data = np.arange(1, 51)

# # 밑 그림
# fig, axes = plt.subplots(2, 3)

# axes[0, 0].plot(data)
# axes[0, 1].plot(data * data)
# axes[0, 2].plot(data ** 3)
# axes[1, 0].plot(data % 10)
# axes[1, 1].plot(-data)
# axes[1, 2].plot(data // 20)

# print(fig) ## canvas 정보

# plt.tight_layout() ## 예쁘게 표현하기 위한 설정.
# plt.show()

# ## 타이틀 설정
# plt.plot([1, 2, 3], [3, 6, 9])
# plt.plot([1, 2, 3], [2, 4, 9])
# # 타이틀 설정
# plt.title('이것은 타이틀 입니다')

# plt.show()

# # 타이틀 font 키우기
# plt.plot([1, 2, 3], [3, 6, 9])
# plt.plot([1, 2, 3], [2, 4, 9])
# # 타이틀 & font 설정
# plt.title('타이틀 fontsize를 키웁니다', fontsize=20)
# # dictionary 변수 선언 시 ' key : value ' 형태 , Dictionary로 사용할때는 대입연산자 key = value 사용

# plt.show()

# ## Legend 설정
# plt.plot(np.arange(10), np.arange(10)*2)
# plt.plot(np.arange(10), np.arange(10)**2)
# plt.plot(np.arange(1, 10), np.log(np.arange(1, 10)))

# # 타이틀 & font 설정
# plt.title('범례 설정 예제입니다', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# # legend 설정
# plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

# ## Limit 설정
# plt.plot(np.arange(10), np.arange(10)*2)
# plt.plot(np.arange(10), np.arange(10)**2)
# plt.plot(np.arange(1, 10), np.log(np.arange(1, 10)))

# # 타이틀 & font 설정
# plt.title('이것은 타이틀 입니다', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# # legend 설정
# plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

# # x, y limit 설정
# plt.xlim(0, 5)
# plt.ylim(0.5, 10)

# plt.show()

# ### Marker 설정
# ### https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# plt.plot(np.arange(10), np.arange(10)*2, marker='o', markersize=5)
# plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', markersize=10)
# plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', markersize=15)
# plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', markersize=20)

# # 타이틀 & font 설정
# plt.title('마커 설정 예제', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# plt.show()

# ## inline 종류
# plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='')
# plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='o', linestyle='-')
# plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='v', linestyle='--')
# plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='+', linestyle='-.')
# plt.plot(np.arange(10), np.arange(10)*2 - 40, marker='*', linestyle=':')

# # 타이틀 & font 설정
# plt.title('다양한 선의 종류 예제', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# plt.show()

# ## color
# plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
# plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='—', color='c')
# plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
# plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# # 타이틀 & font 설정
# plt.title('색상 설정 예제', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# plt.show()

# # opacity 설정
# plt.plot(np.arange(10), np.arange(10)*2, color='b', alpha=0.1)
# plt.plot(np.arange(10), np.arange(10)*2 - 10, color='b', alpha=0.3)
# plt.plot(np.arange(10), np.arange(10)*2 - 20, color='b', alpha=0.6)
# plt.plot(np.arange(10), np.arange(10)*2 - 30, color='b', alpha=1.0)

# # 타이틀 & font 설정
# plt.title('투명도 (alpha) 설정 예제', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# plt.show()

# # grid 옵션 추가
# plt.grid()

# plt.show()

# ## 이미지 저장
# plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
# plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
# plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
# plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# # 타이틀 & font 설정
# plt.title('그리드 설정 예제', fontsize=20)

# # X축 & Y축 Label 설정
# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축', fontsize=20)

# # X tick, Y tick 설정
# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# # grid 옵션 추가
# plt.grid()

# # 이미지 저장
# plt.savefig('my_graph.png', dpi=300)

# plt.show()

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# ## 임의의 랜덤값 생성
# np.random.rand(50)
# ## 0부터 50개의 값을 순차적으로 생성
# np.arange(50)

# ###
# ### 1. Scatterplot
# ### 
# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.arange(50)
# area = x * y * 1000

# plt.scatter(x, y, s=area, c=colors) ## s = size, c = color
# plt.show()


# ###
# ### cmap, alpha
# ###
# np.random.rand(50)

# plt.figure(figsize=(12, 6))

# plt.subplot(131)
# plt.scatter(x, y, s=area, cmap='blue', alpha=0.1)
# plt.title('alpha=0.1')

# plt.subplot(132)
# plt.title('alpha=0.5')
# plt.scatter(x, y, s=area, cmap='blue', alpha=0.5)

# plt.subplot(133)
# plt.title('alpha=1.0')
# plt.scatter(x, y, s=area, cmap='blue', alpha=1.0)

# plt.show()





# ###
# ### 2. Barplot
# ### 
# x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
# y = [66, 80, 60, 50, 80, 10]

# plt.figure(figsize=(6, 3))
# # plt.bar(x, y) ## 간단히.
# plt.bar(x, y, align='center', alpha=0.7, color='red')
# plt.xticks(x)
# plt.ylabel('Number of Students')
# plt.title('Subjects')

# plt.show()


# ###
# ### 2-2. 기본 Barhplot 그리기
# ### 
# x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
# y = [66, 80, 60, 50, 80, 10]

# plt.barh(x, y, align='center', alpha=0.7, color='green')
# plt.yticks(x)
# plt.xlabel('Number of Students')
# plt.title('Subjects')

# plt.show()


# ###
# ### Batplot에서 비교 그래프 그리기
# ###
# x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
# x = np.arange(len(x_label))
# y_1 = [66, 80, 60, 50, 80, 10]
# y_2 = [55, 90, 40, 60, 70, 20]

# # 넓이 지정, bar의 넓이 지정
# width = 0.35

# # subplots 생성
# fig, axes = plt.subplots()

# # 넓이 설정
# axes.bar(x - width/2, y_1, width, align='center', alpha=0.5)
# axes.bar(x + width/2, y_2, width, align='center', alpha=0.8)

# # xtick 설정
# plt.xticks(x)
# axes.set_xticklabels(x_label)

# # label 설정
# plt.ylabel('Number of Students')
# plt.title('Subjects')

# plt.legend(['john', 'peter'])

# plt.show()


# ###
# ### Batplot에서 비교 그래프 그리기
# ###
# x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
# x = np.arange(len(x_label))
# y_1 = [66, 80, 60, 50, 80, 10]
# y_2 = [55, 90, 40, 60, 70, 20]

# # 넓이 지정
# width = 0.35

# # subplots 생성
# fig, axes = plt.subplots()

# # 넓이 설정
# axes.barh(x - width/2, y_1, width, align='center', alpha=0.5, color='green')
# axes.barh(x + width/2, y_2, width, align='center', alpha=0.8, color='red')

# # xtick 설정
# plt.yticks(x)
# axes.set_yticklabels(x_label)
# plt.xlabel('Number of Students')
# plt.title('Subjects')

# plt.legend(['john', 'peter'])

# plt.show()





# ###
# ### 3. Lineplot
# ###
# x = np.arange(0, 10, 0.1)
# y = 1 + np.sin(x)

# plt.plot(x, y)

# plt.xlabel('x value', fontsize=15)
# plt.ylabel('y value', fontsize=15)
# plt.title('sin graph', fontsize=18)

# plt.grid()

# plt.show()


# ###
# ### 두 개이상의 Lineplot
# ###
# x = np.arange(0, 10, 0.1)
# y_1 = 1 + np.sin(x)
# y_2 = 1 + np.cos(x)

# plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3)
# plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7)

# plt.xlabel('x value', fontsize=15)
# plt.ylabel('y value', fontsize=15)
# plt.title('sin and cos graph', fontsize=18)

# plt.grid()
# plt.legend()

# plt.show()


# ###
# ### Marker Lineplot
# ###
# x = np.arange(0, 10, 0.1)
# y_1 = 1 + np.sin(x)
# y_2 = 1 + np.cos(x)

# plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3, marker='o')
# plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7, marker='+')

# plt.xlabel('x value', fontsize=15)
# plt.ylabel('y value', fontsize=15)
# plt.title('sin and cos graph', fontsize=18)

# plt.grid()
# plt.legend()

# plt.show()


# ###
# ### Line Style
# ###
# x = np.arange(0, 10, 0.1)
# y_1 = 1 + np.sin(x)
# y_2 = 1 + np.cos(x)

# plt.plot(x, y_1, label='1+sin', color='blue', linestyle=':')
# plt.plot(x, y_2, label='1+cos', color='red', linestyle='-.')

# plt.xlabel('x value', fontsize=15)
# plt.ylabel('y value', fontsize=15)
# plt.title('sin and cos graph', fontsize=18)

# plt.grid()
# plt.legend()

# plt.show()