# pip install matplotlib
import matplotlib.pyplot as plt

# x_years = ['2020', '2021', '2022']
# y_data = [100, 400, 900]
# clr = ["r", "g", "b"]

# plt.bar(x_years, y_data)

# 수평 그래프 그리기
# plt.barh(x_years, y_data)

# 그래프 설정
#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
# plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

# 막대문양 채우기
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="////")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="o")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="x")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="..")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="...")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="....")


# 산점도 그래프 그리기
# x_data = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# y_data = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

# plt.plot(x_data, y_data)

# x = 1
# y = 1
# plt.scatter(x, y)
# plt.scatter(x+1, y+1)
# plt.scatter(x+2, y+1)
# plt.scatter(x+3, y+1)
# plt.scatter(x+3, y+2)
# plt.scatter(x+3, y+1)

# 포인트 설정
#         {x}{y}{포인트크기}{색상설정}{투명}
# plt.scatter(x+1.5, y+1.5, 100, 2, alpha=0.5)


# 컬러맵 설정
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="viridis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="magma")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="infermo")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
# plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="Set1")
# plt.colorbar()


# 히스토그램 그리기
# plt.hist({data}, bins={구간수})
# import numpy as np
# rn = np.random.randint(1, 30, size=20)
# print(rn)

# 라벨 설정
# plt.hist(rn, bins=10, label="def")

# 투명도 설정
# plt.hist(rn,  bins=10, label="def", alpha=0.5)
# plt.hist(rn,  bins=5, label="def", alpha=0.5)

# 그래프 스타일 설정
# plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")
# plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="stepfilled")
# plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="barstacked")

# plt.legend()
# plt.show()
 
# 파이챠트 그리기
# rate = [30, 40, 20, 10]
# labels = ["Alpha", "Beta", "famma", "Delta"]

# plt.pie({data})
# plt.pie(rate)

# 라벨 표시
# plt.pie(rate, labels=labels)

# 퍼센트 표시
# plt.pie(rate, labels=labels, autopct='%.1d%%')
# plt.pie(rate, labels=labels, autopct='%.1f%%')

# 시작각도 설정
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270)

# 시작방향설정
#                                                            시계방향으로 시작
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=True)

# 공백설정
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.1])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0])


# 패널스타일 설정
# 사용가능한 스타일 키
# print(plt.style.available)

# plt.plot([2,3,6,7,10], [1,4,5,8,9])
# plt.style.use("bmh")
# plt.style.use("ggplot")
# plt.style.use("classic")
# plt.style.use("Solarize_Light2")
# plt.style.use("dark_background")
# plt.style.use("fast")


# 포멧설정
# plt.plot([2,3,6,7,10], [1,4,5,8,9])

# 패널 사이즈 적용
# plt.rcParams['figure.figsize'] = (6, 3)
# plt.rcParams['figure.figsize'] = (4, 3)

# 전체 폰트 사이즈 적용
# plt.rcParams['font.size'] = 20

# 선 두께 설정
# plt.rcParams['lines.linewidth'] = 5
# plt.rcParams['lines.linewidth'] = 15 # ???

# 선 스타일 설정
# plt.rcParams['lines.linestyle'] = '-'
# plt.rcParams['lines.linestyle'] = '--'

# 눈금 설정
# 위 눈금 설정
# plt.rcParams['xtick.top'] = True

# # 오른 눈금 설정
# plt.rcParams['ytick.right'] = True

# # 안쪽으로 눈금 설정
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'

# # 눈금 길이
# plt.rcParams['ytick.major.size'] = 12

# # 세부 눈금
# plt.rcParams['xtick.minor.visible'] = True

# plt.plot([2,3,6,7,10], [1,4,5,8,9])


# 객체 활용
# fig, ax = plt.subplots()
# ax = fig.add_axes([0, 0, 0, 0])
# ax = fig.add_axes([1, 1, 0, 0])
# ax = fig.add_axes([1, 1, 1, 1])


# 다중 패널 객체 생성
# fig, ax = plt.subplots(1, 1)
# fig, ax = plt.subplots(1, 2)
# fig, ax = plt.subplots(2, 1)
# fig, ax = plt.subplots(2, 2)
# fig, ax = plt.subplots(3, 2)
# fig, ax = plt.subplots(3, 3)

# plt.tight_layout()

# 다중 패널 그래프 출력
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]

# fig, ax = plt.subplots(2, 2)

# ax[0][0].plot(x, y1)
# ax[1][0].plot(x, y1)
# ax[0][1].plot(x, y1)
# ax[1][1].plot(x, y1)

# 축 공유
# fig, ax = plt.subplots(2, 2, sharex=True)
# fig, ax = plt.subplots(2, 2, sharey=True)

# ax[0][0].plot(x, y1)
# ax[1][0].plot(x, y1)
# ax[0][1].plot(x, y1)
# ax[1][1].plot(x, y1)


# Y축 동시 출력
# 사용 데이터
# x = [1,4,5,8,9]

# y1 = [2,3,6,7,10]
# y2 = [10,8,6,4,2]

# fig, ax1 = plt.subplots()
# ax1.set_xlabel("X-Data")
# ax1.set_ylabel("Y1")
# # ax1.plot(x, y1)

# ax2 = ax1.twinx()
# ax2.set_ylabel("Y2")
# # ax2.plot(x, y2)

# ax1 / ax2 개별 색상 설정
# ax1.plot(x, y1, color="C1")
# ax2.plot(x, y2, color="C2")

# ax1 / ax2 개별 라벨 출력
# ax1.plot(x, y1, color="C1", label="y1 Data")
# ax1.legend(loc="upper right")

# ax2.plot(x, y2, color="C2", label="y2 Data")
# ax2.legend(loc="upper left")


# 이종 그래프 출력, 라벨 출력
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1", label="XData")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2", label="YData")
ax2.set_ylabel("Y2data")

ax1.legend(loc="upper right")
ax2.legend(loc="upper left")



# plt.legend() #라벨에 안붙이면 안돼!
# plt.tight_layout() #다중그래프 적당한 거리감 출력

plt.show()

