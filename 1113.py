# 복습_경로data

# body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a
# content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong

""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")

print(item)
print(item.get_text())

print(wt)
print(wt.get_text())

print(goods)
print(goods.get_text()) """



""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss = res_html.select("a.wrap_thumb")
# print(iss)
print("\n---------------------------------\n")

for i in iss :
    issue = i.get_text()
    print(issue)
    
print("\n---------------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct:
    c = j.attrs["data-tiara-custom"]
    print(c + "\n") """
    
    
# 이미지 저장
from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrieve as rl

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

imgs = res_html.select("img")

linkimgs = []

for i in imgs:
    irs = i.attrs["src"] 
    linkimgs.append(irs)
    
folder = "imgs/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
i = 0
for ln in linkimgs :
    if str(ln).find("//t") == False:
        print(ln)
        continue
    else:
        pass
    i += 1
    rl(ln, folder + f"{i}.jpg")
    
    # print(ln)
    # linkimgs.append(img.attrs["src"])

# Pandas 전처리

# Series 
""" : pandas 에서 사용하는 일차원 데이터 관리하는 데이터 자료구조로, 
파이썬의 리스트와 유사하고 인덱스를 갖고 있어 
인덱싱과 슬라이싱을 사용할수 있습니다 """

# 인덱스(index)
## 특정 데이터 구조내에 색인, 순서, 구분등을 구성해 동작 속도를 높여주는 장치

# 인덱싱(indexing) : 가르키다
## 연속적인 자료구조내 index를 활용해 값을 추출하거나 처리하는 메카니즘

# 슬라이싱(slicing) : 잘라내다
## 연속적인 자료구조내 index를 활용해 특정 범위, 특정 구간을 추출하는 메카니즘

#import pandas.Series
""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)

print(sdata) """

# numpy를 이용한 데이터 생성
""" from pandas import Series as sr
import numpy as np


data = np.arange(1, 5)
sdata = sr(data)

print(sdata) """


# 인덱스 설정 확인
""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)

print(sdata.index)
# print(sdata.index.to_list()) # 값을 세세하게 보고 싶다! """


# 인덱스 설정
""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)
print(sdata)
print("\n---------------------------------------\n")

sdata.index = ["a", "b", "c", "d"]
print(sdata) """


# 인덱스 생성1
""" from pandas import Series as sr
data = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

sdata = sr(data, idx)
print(sdata) """


# 인덱스 생성2
""" from pandas import Series as sr
dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

# sd = sr(dt, idx)
# print(sd)

# sdata = sr(data=dt, index=idx)
# sdata = sr(data=idx, index=dt)
# sdata = sr(dt, idx)
sdata = sr(idx, dt)
print(sdata) """

# 인덱스 생성3
""" from pandas import Series as sr
dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

sdata = sr(data=dt, index=idx)
# print(sdata)

# sd = sdata.reindex(["a", "j", "c"])
# sd = sdata.reindex(["a", "c"])
# print(sd) 

sd = sdata.reindex(["b"])
print(sd) 
print("\n------------------------\n")
print(sdata["b"])
print("\n------------------------\n")

print(sdata.iloc[0])
print(sdata.iloc[2])
print("\n------------------------\n")
print(sdata.loc["a"])
print(sdata.loc["b"]) """

# print(sdata[0]) # error


# 인덱싱슬라이싱
""" from pandas import Series as sr

dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]

sdata = sr(data=dt, index=idx)

print(sdata.loc["bc":"cd"])
print("\n------------------------\n")
print(sdata.loc["bc":])
print("\n------------------------\n")
print(sdata.loc[:"bd"]) """


# 인덱싱슬라이싱_한글
""" from pandas import Series as sr

dt = ["사과", "바나나", "수박", "참외"]
idx = ["가", "나", "다", "라"]

sdata = sr(data=dt, index=idx)

print(sdata.iloc[1:2])
print("\n------------------------\n")
print(sdata.iloc[2:])
print("\n------------------------\n")
print(sdata.iloc[:2]) """


# 수정/추가/삭제
## 수정
""" from pandas import Series as sr

dt = ["alpha", "beta", "charlie", "delta"]
idx = ["ab", "bc", "cd", "de"]

sdata = sr(data=dt, index=idx)

sdata.loc["cd"] = "echo"
print(sdata)

print("\n------------------------\n")
sdata.iloc[1] = "fox"
print(sdata)

## 추가
sdata.loc["ef"] = "golf"
print(sdata)

## 삭제
print("\n------------------------\n")
print(sdata.drop("bc"))
# or
sdata = sdata.drop("bc")
print(sdata) """

# 연산
## 시리즈에서 사칙연산 및 속성 연산을 지원합니다.
""" from pandas import Series as sr
s1 = sr([100, 200, 300], index=["a", "b", "c"])
s2 = sr([100, 200, 300], index=["b", "c", "a"])

sum_res = s1 + s2
print(sum_res)
print(sum_res.max())
print(sum_res.mean())
print(sum_res.min())
print("\n------------------------\n")

sub_res = s1 - s2
print(sub_res)
print(sub_res.max())
print(sub_res.mean())
print(sub_res.min())
print("\n------------------------\n")

mul_res = s2 * 10
print(mul_res)

div_res = s1 / 10
print(div_res) """

# 데이터 연산
""" from pandas import Series as sr

data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

sdata = sr(data)
uniq = sdata.unique()
print(uniq)

sc = sdata.count()
print(sc)

sv = sdata.value_counts()
print = sv """


# 필터링
## 시리지는 여러가지 조건을 적용해 데이터를 처리할 수 있습니다.
""" from pandas import Series as sr

idx = ["a", "b", "c", "d", "e"]
s1 = sr([1100, 270, 30, 450, 50], index=idx)
s2 = sr([150, 740, 810, 40, 25], index=idx)

# 시리즈내 데이터 비교
fil = s1 > 300
print(fil)

print("\n------------------------\n")
print(s1[fil].index)

# 시리즈간 비교
print("\n------------------------\n")
fil1 = s2 > s1
print(fil1)

print(s2[fil1])

# 인덱싱 출력
print("\n------------------------\n")
print(s2[s2 > s1].index) """


# 정렬
## 데이터 정렬
from pandas import Series as sr

idx = ["a", "b", "c", "d", "e"]
dt = [1100, 270, 30, 450, 50]
s1 = sr(data=dt, index=idx)

#오름차순
sv = s1.sort_values()
print(sv)
print("\n------------------------\n")

# 내림차순
sv1 = s1.sort_values(ascending=False)
print(sv1)