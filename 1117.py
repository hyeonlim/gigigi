#Dataframe
"""
import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

print(df)
print(df[1])
print(df[1][1])

#dictionary

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

#출력
print(fr)
print(fr["x"])
print(fr.x)
print(fr.iloc[2])
print(fr.loc["y축"])

#컬럼(열)추가
frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
frs["t"] = [60, 120, 180]

#행 추가
frs.loc["t축"] = [100, 200, 300, 400]

#행 수정
frs.loc["t축"] = [500, 600, 700, 800]

#행 / 열 삭제

#행 삭제
frs.drop("x", axis=1, inplace=True)

# 열 삭제
frs.drop("x축", inplace=True)

#NA : 사용할 수 없는 값
#Not Available 값은 있으나 인식할 수 없는 경우 (cf_null-데이터가 없는경우)

#컬럼(열)추가

dt = [[1,10,100],[2,20,200],[3,30,300]]
ol =["col1", "col2", "col3"]
idx = ["x축","y축","z축"]

df = pd.DataFrame(data=dt,index=ol,columns=idx)

#컬럼 / 행 출력
#print(df["col1"])
#인덱스 / 로우 출력
print(df.loc["x축"])
#연산
print(df + 1)
print(df.div(100))
print(df / 100)
print(df.mul(100))

#두 데이터프레임간 연산

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","엘지"],columns=["col2"])

print(df2)

print("\n--------------\n")
print(df.div(df2))
print("\n--------------\n")
print(df.mul(df2))
print("\n--------------\n")
#빈값을 채워 연산
print(df.div(df2, fill_value=100))
"""
#멀티인덱스
"""
import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

#출력
print(df.loc["row1"])
print(df.loc["row2"])
print(df.iloc[0])

#엘레멘트 출력
print(df.loc[("row3", "val3"), "col1"])

#랜덤 데이터 생성

import numpy as np

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

#출력
print(df[2])
print(df.loc[2])
print(df.loc[3][1])

#범위 출력
print(df.head(3))
print(df.tail(3))

#샘플
print(df.sample)
"""
#출력
"""
from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name)

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
"""
#with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
#    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")
"""
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
            temp.color_name() + "\n")
"""
#파일열기
"""
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

print(df)

print(df.values[0])

#인덱스 설정 확인

print(df.index)

print(df.dtypes)

print(type(df))

#부분읽기
print("\n--------------\n")
print(df.head())
print("\n--------------\n")
print(df.head(3))

#끝에서 부터 부분 읽기
print("\n--------------\n")
print(df.tail())
print("\n--------------\n")
print(df.tail(3))

#sampling 
print(df.sample())
print(df.sample(4))

#인덱스 설정 확인
print(df.index)

#컬럼별 타입확인
print(df.dtypes)

#엘레멘트 출력
for el in df.values[12] :
    print(el)
    
#데이터프레임 정보확인
print(df.info())

#출력
print(df.values)
print(df.values[3])

#null 값 확인
print(df.isnull())
print(df.isnull().sum())

#컬럼 / 행 데이터 확인
print(df.name)
print(df.postcode)
print(df.job)
print(df.phone)
print(df.id)
print(df.company)
print(df.catch_parase)
print(df.color)

print(df["name"])
print(df["postcode"])
print(df["job"])
print(df["phone"])
print(df["id"])
print(df["company"])
print(df["catch_parase"])
print(df["color"])

#여러 컬럼 확인
print(df[["name", "id"]])
print(df[["name", "address", "postcode"]])

#컬럼 데이터 상세
print(df.postcode.describe())
print(df.color.describe())

#컬럼 데이터 갯수
print(df.color.count())

# 각 데이터별 카운팅
print(df.color.value_counts())

#데이터간 연산
temp = df.postcode.sum() / df.name.count()
print(temp)

#비교 연산 
df.name == "쿵철이"

#temp = df[df.color =="Ivory"].head(1)
temp = df[df.color =="Ivory"].head(2)
print(temp)
"""