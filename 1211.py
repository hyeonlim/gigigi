import matplotlib.pyplot as plt


# 이종 그래프 출력, 라벨 출력
# x = [1,4,5,8,9]
# y1 = [2,3,6,7,10]
# y2 = [2,3,6,7,10]

# fig, ax1 = plt.subplots()

# ax1.plot(x, y1, "-o", color="C1", label="XData")
# ax1.set_xlabel("X")
# ax1.set_ylabel("Ydata")

# ax2 = ax1.twinx()
# ax2.bar(x, y2, color="C2", label="YData")
# ax2.set_ylabel("Y2data")

# ax1.legend(loc="upper right")
# ax2.legend(loc="upper left")


# 다중 그래프 출력
# 사용데이터
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

# 각 패널 별 스타일 지정
# plt.style.use("bmh")

# plt.subplot(2, 1, 1)    # 1set
# plt.subplot(1, 2, 1)
# plt.subplot(3, 1, 1)
# plt.plot(x1, y1, "o-")

# plt.title("x1 Graph")
# plt.xlabel("x-data")
# plt.ylabel("y-data")

# plt.subplot(2, 1, 2)    # 2set
# plt.subplot(1, 2, 2)
# plt.subplot(3, 1, 2)
# plt.plot(x2, y2, ".-")

# plt.title("x1 Graph")
# plt.xlabel("x-data")
# plt.ylabel("y-data")

# plt.subplot(3, 1, 3)
# plt.plot(x2, y2, ".-")

# 결과 이미지 저장
# plt.savefig("data/img.jpg")
# plt.savefig("data/img.png")

# 2행 2열(row) 그래프 출력
# plt.subplot(2, 2, 1)
# plt.subplot(2, 2, 2)
# plt.subplot(2, 2, 3)
# plt.subplot(2, 2, 4)


# 다중 객체를 이용한 막대 그래프 출력
# x_years = ["2020", "2021", "2022"]
# y_data = [100, 400, 900]

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# ax1.bar(x_years, y_data)
# ax2.bar(x_years, y_data)
# ax3.bar(x_years, y_data)
# ax4.bar(x_years, y_data)

# ax1.bar(x_years, y_data, color="aquamarine", edgecolor="black", hatch="/")
# ax2.bar(x_years, y_data, color="salmon", edgecolor="black", hatch="\\")
# ax3.bar(x_years, y_data, color="navajowhite", edgecolor="black", hatch="+")
# ax4.bar(x_years, y_data, color="lightskyblue", edgecolor="black", hatch="*")

# plt.tight_layout()
# plt.show()


# =====================================
import seaborn as sns
# pip install seaborn
import pandas as pd

# 전체 요금과 팁의 상관관계에 대한 산점도와 선형그래프 출력
# tips = sns.load_dataset("tips")
# print(tips)
# sns.regplot(x="total_bill", y="tip", data=tips)

# plt.show()

# tips = sns.load_dataset("tips")
# print(tips)
# sns.regplot(x="total_bill", y="tip", data=tips)
# sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
# sns.barplot(x="tip", y="total_bill", data=tips)
# sns.barplot(x="sex", y="total_bill", data=tips)
# sns.barplot(x="sex", y="tip", data=tips)
# sns.barplot(x="smoker", y="total_bill", data=tips)
# sns.barplot(x="smoker", y="tip", data=tips)
# sns.barplot(x="time", y="total_bill", data=tips)

# plt.title("Average Tips")
# plt.xlabel("x")
# plt.ylabel("Average")


# 타이타닉 데이터
# titanic = sns.load_dataset("titanic")
# sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

# 탑승클래스별 인원구성
# sns.countplot(x="class", hue="who", data=titanic)

# 클래스별 생존자
# sns.countplot(x="class", hue="alive", data=titanic)

# 성별별 생존자
# sns.countplot(x="sex", hue="alive", data=titanic)

# 싱글 여행자별 인원구성
# sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별
# sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)

# plt.show()


# 주식데이터 분석
import FinanceDataReader as fdr

# df = fdr.DataReader("KS11")
# df0 = df.loc["2023"]

# print(df0)

# df0["Open"].plot()
# df0["High"].plot()
# df0["Low"].plot()
# df0["Close"].plot()

# plt.grid(True)


# 다우지수와 코스피 비교
dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# 각 지수별 종가 기준 그래프 출력
# plt.plot(dow.index, dow.Close, "r--", label="Dow")
# plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

# plt.plot(dow.index, dow.High, "r--", label="Dow")
# plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

# d = (dow.Close.loc["2010-06-01"])*100
# k = (kospi.Close.loc["2010-06-01"])*100
# plt.plot(dow.index, dow.Close, "r--", label="Dow")
# plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")
# plt.legend()

# plt.grid(True)
# plt.show()


# 국내 개별 종목 분석
# 해당 데이터를 가져오는 URL
# code 는 종목명
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs

# 해당 데이터를 가져오는 URL
# code 는 종목명
url = "https://finance.naver.com/item/sise_day.nhn?code=005930"

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)

df_list =[]
page = 1
for page in range(1, 10):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break

print(df_list)

df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.plot(df["날짜"], df["종가"], "co-")

""" 아앙? 어이 - 예쁜이 이쪽 좀 보라고~~  """