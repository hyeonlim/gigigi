""" from faker import Faker as fk
import os

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)

temp = fk("ko-KR")
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n") """
        
""" import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/apt.csv", encoding="utf8")

print(df.head()) """

import pandas as pd

df = pd.read_csv("./data/apt.csv", index_col=0)

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})

df["분양가"] = df["분양가"].convert_dtypes()

print(df.dtypes)
print("\n---------------------\n")

# 정렬
# res = df.sort_values(by="지역명")
# res = df.sort_values("지역명")
# res = df.sort_values("지역명", ascending=True)  # 오름차순
# res = df.sort_values("지역명", ascending=False)  #내림차순
# print(res.head(5))
# print(res.head()) # 헤드의 기본값은 5개

# res = df.sort_values(by="연도")
# res = df.sort_values(by="분양가")
# res = df.sort_values(by="연도")[:5]
# res = df.sort_values(by="연도")[10:20]
# print(res) 

# 컬럼이름 출력
# res = df["지역명"][:5]
# res = df[["지역명", "연도"]]
# res = df[["지역명", "연도", "분양가"]] # 분양가로 표기하는 작업이 있어야 핸들링이 됨
# res = df[["지역명", "연도", "분양가"]][:7]
# print(res)

# res = df.loc[:, ["지역명", "연도", "분양가"]][:5]
# res = df.loc[:][:5]
# res = df.loc[:][:]
# res = df.iloc[1]
# print(res)

# res = df.loc[6:, ["지역명", "연도"]]
# res = df.loc[6:, ["지역명", "연도"]][:7] # 6부터 7개
# res = df.loc[:3, ["지역명", "연도"]][:8]  #앞에 쓰이는게 우선시 됨
# print(res)

# 필터 출력
# res = df.loc[df["지역명"]=="강원"]
# res = df.loc[df["연도"] > 2020]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:] #끝에서부터
# print(res)

df0 = df.copy()
# print(df0)

# 인덱스 지정 선택
# res = df.iloc[2]
# res = df.iloc[2][2]
# print(res)

# res = df[df.index > 3560]
# print(res)

# 필터
# res = df[df.연도 == 2023]
# res = df[df.월 == 3]
# print(res)

# 비트연산 필터
# res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
# print(res)

# 컬럼 추가
# columns = list(df.columns)
# print(columns + "컬럼")

df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
# print(df)
# print("\n--------------\n")
# print(df1)

print("\n--------------\n")
# df1.loc[:6, "extra"] = "0"
# df1.loc[:4, "extra"] = False
# print(df1)

#복사
df2 = df1.copy()

# NaN 행 제거
# res = df2.dropna(how="any")
# res = df2.fillna(value="1234")
# res = df2.fillna(value="1234", inplace=True)
# print(df2)
# print("\n--------------\n")
# res = df2.dropna(how="any", inplace=True)
# print(res)
# print("\n--------------\n")
# print(df2)

# NaN 데이터 출력
# res = pd.isna(df1)
# res = pd.isna(df)
# res = pd.isna(df0)
# res = pd.isna(df2)
# print(res)

# 데이터 종류별 출력
# res = df["연도"].value_counts()
# res = df["지역명"].value_counts()
# res = df["월"].value_counts()
# res = df.월.value_counts()
# print(res)

# 그룹핑
# res = df.groupby(["지역명", "연도", "월"]).sum()
# res = df.groupby(["지역명", "연도", "월"])["분양가"].all
# print(res)

res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)

