# 클래스 복습
""" import calc as cm

cl = cm.Calc()

print(cl.add(1,2)) """


# 8. 모듈, 라이브러리 활용

# 문자열 처리
# 1. 줄임말 처리
# textwarp.shorten - 단어 단위로 문자열을 줄여주는 기능
""" import textwrap as tw

targetText = "동해물과 백두산이 마르고"
# targetText = "To be or not to be, That is a question!"

res = tw.shorten(targetText, width=10)  # 10문자로 잘라라
print(res) """


# 2. 줄 바꿈 처리
# textwarp.wrap - 긴 문자를 줄바꿈 처리, 리스트로 반환
""" import textwrap as tw

target = "To be or not to be, That is a question!"
longTarget = target * 200

print(longTarget)
print("\n===========================\n")

res = tw.wrap(longTarget, width = 50)
print(res)  # list로 출력이 됨, 반환되었음 """

# join() 함수 추가, 출력
""" print("\n===========================\n")

res = ('\n'.join(res))
print(res)  #잘라진 형태의 텍스트 출력 """

# fill() 함수로 처리
# 앞의 두 단계 필요없이 한번에 같은 결과가 나옴
""" import textwrap as tw

target = "To be or not to be, That is a question!"
longTarget = target * 200

res = tw.fill(longTarget, width = 50)

print(res) """


# 3. 문자열 치환
# 특정 문자를 치환 예) 주민등록번호 등
""" line = "홍길동의 주민번호는 012345-1234567 입니다. "
word_result = []

for word in line.split(" "):
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
        word = word[:6] + "-" + "*******"
    word_result.append(word)
print(" ".join(word_result)) """

# 정규식 표현
## re 모듈을 활용, 정규표현식을 컨트롤
""" import re
line = "홍길동의 주민번호는 012345-1234567 입니다."
res = re.compile("(\d{6})[-]\d{7}")
print(res.sub("\g<1>-*******", line))  #치환 """

# 날짜 처리
## datetime 모듈을 이용한 날짜 처리
""" import datetime as dt

day1 = dt.date(2023, 11, 3)
print(day1)

day2 = dt.date(2000, 10, 24)
print(day2) """

#날짜 계산
""" diff = day1 - day2  #플러스는 델타타임을 이용해서 하는걸로..?
print(diff) """

# 날짜 객체1
## 날짜 데이터를 객체화하여 처리
""" import datetime as dt

res = dt.datetime(2023, 11, 1, 12, 30, 40)
tHour = res.hour
tMin = res.minute
tSec = res.second

print(res, tHour, " ", tMin, " ", tSec) """

# 날짜 객체2
## 2개의 객체를 합쳐서 표현
""" import datetime as dt

day = dt.date(2023, 11, 1)
time = dt.time(12, 30, 40)

res = dt.datetime.combine(day, time)
print(res) """

# 요일 판별
## 해당 날짜가 어떤 요일인지 판별
""" import datetime as dt

day = dt.date(2023, 11, 1)  #참고로 11월 1일은 수요일
res = day.weekday()
print(res)  # 0=월 1=화 2= 수 [...] 6=일

yesterday = dt.date(2023, 10, 31)
res1 = yesterday.weekday()
print(res1) """

# 날짜 세기
""" import datetime as dt

today = dt.date.today()
print(today)

difday = dt.timedelta(days = 100)  #시간, 분도 가능
print(difday)

print(today + difday) """

# 단어 세기
#collections, re 모듈 사용
""" import re
import collections as cl """

""" poem =  """"""
내가 그의 이름을 불러 주기 전에는
그는 다만
하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러 주었을 때
그는 나에게로 와서
꽃이 되었다.
내가 그의 이름을 불러 준 것처럼
나의 이 빛깔과 향기에 알맞은
누가 나의 이름을 불러 다오.
그에게로 가서 나도
그의 꽃이 되고 싶다.
우리들은 모두
무엇이 되고 싶다.
너는 나에게 나는 너에게
잊혀지지 않는 하나의 눈짓이 되고 싶다."""

""" wd = re.findall(r"\w+", poem)
# print(wd)
print(len(wd))  # 리스트의 길이를 재거라 """

# 많이 사용하는 단어 찾기
## most_common() 활용
""" cnt = cl.Counter(wd)
print(cnt.most_common(1))  #첫번째로 가장 많이 사용된 단어 무엇 안에 넣는 숫자에 따라 달라짐 """

# 정렬 출력
## pprint 모듈을 이용해 정렬 출력
""" import pprint

data = {"month": "9", "num": 642, "link": "", "year": "2009", "news": "", "safe_title": "Creepy", "transcript": "[[Two people are sitting on chairs.]]\nMan: Hey, cute netbook.\nWoman: \nWhat.\n\n\nMan: Your laptop. I just --\nWoman: No, why are you talking to me.\n\nWoman: Who do you think you are? If I were even slightly interested, I'd have shown it.\n\nWoman: Hey everyone, this dude's hitting on me.\nVoice #1: Haha\nVoice #2: Creepy\nVoice #3: Let's get his picture for Facebook to warn others.\n\n((This panel fades into a thought bubble of the actual man.))\n[[The girl is typing on her laptop.]]\nDear blog,\nCute boy on train still ignoring me.\n\n{{Title text: And I even got out my adorable new netbook!}}", "alt": "And I even got out my adorable new netbook!", "img": "https://imgs.xkcd.com/comics/creepy.png", "title": "Creepy", "day": "28"}
print(data)
pprint.pprint(data) """

# 수학문제
## math 모듈 활용

# 최대공약수(greatest common divisor)
""" import math
res = math.gcd(60, 100, 80)
print(res, "봉지") """

# 최소공배수(least common multiple)
""" import math
res = math.lcm(15, 25)
print(res, "분") """

# 로또 번호 생성
## random 모듈 활용
""" import random

res = []
while len(res) < 6:
    num = random.randint(1, 45)
    if num not in res:
        res.append(num)
print(res) """

# 통계
## statistics 모듈을 활용

# 평균값 구하기
""" import statistics

data = [48, 92, 57, 59, 63, 83, 56, 91, 82, 74, 63, 72]
print(statistics.mean(data)) """

# 중간값 찾기
""" print(statistics.median(data)) """

# 압축하기
## zlib 모듈을 이용해 압축 처리

# 압축하기
""" import zlib
data = "To be or not to be, That is a question!"
longData = data * 100

print(len(longData))
print("\n===============================\n")

cmp = zlib.compress(longData.encode(encoding="utf-8"))
print(cmp)
print("\n===============================\n")
print(len(cmp)) """

# 압축해제
""" decmp = zlib.decompress(cmp).decode("utf-8")
print(decmp)

print("\n===============================\n")
print(len(decmp)) """

# 파일 압축 저장
## gzip 모듈 활용

# 압축 저장하기
""" import gzip

data = "To be or not to be, That is a question!" * 10000
print(len(data))

with gzip.open('data.txt.gz', 'wb') as fp:
    fp.write(data.encode('utf-8'))
 """

# 압축 읽기
""" with gzip.open('data.txt.gz', 'rb') as fp:
     read_data = fp.read().decode('utf-8')
     print(read_data) """
     
# 압축 2
## bz2 모듈을 이용해 파일 압축

# 압축하기
""" import bz2

data = "To be or not to be, That is a question!" * 10000
cmp = bz2.compress(data.encode(encoding="utf-8"))
print(len(data))

print(cmp)
print("\n===============================\n")
print(len(cmp)) """

# 해제하기
""" decmp = bz2.decompress(cmp).decode("utf-8")

print(decmp)
print("\n===============================\n")
print(len(decmp)) """

# 파일 압축
## zipfile 모듈을 활용해 파일 뭉쳐 압축

# 압축하기
""" import zipfile as zf

data = "To be or not to be, That is a question!" * 10000 """

""" fp1 = open("a.txt", "w")
fp1.write(data)
fp1.close()

fp2 = open("b.txt", "w")
fp2.write(data)
fp2.close()

fp3 = open("c.txt", "w")
fp3.write(data)
fp3.close()

with zf.ZipFile('txt.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt') """
    
# 해제하기
""" with zf.ZipFile('txt.zip') as myzip:
    myzip.extractall() """
    
# 파일 압축 2
## tarfile 모듈 활용, zipfile과 동일

# 압축하기
""" import tarfile """

""" data = "To be or not to be, That is a question!" * 10000

fp1 = open("atar.txt", "w")
fp1.write(data)
fp1.close()

fp2 = open("btar.txt", "w")
fp2.write(data)
fp2.close()

fp3 = open("ctar.txt", "w")
fp3.write(data)
fp3.close()

with tarfile.open('txt.tar', 'w') as mytar:
    mytar.add('atar.txt')
    mytar.add('btar.txt')
    mytar.add('ctar.txt') """
    
# 압축해제
""" with tarfile.open('txt.tar') as mytar:
    mytar.extractall() """
    
# 실행 아규먼트
## 프로그램을 실행할때 argparge 모듈을 이용해 처리

# 아규먼트 파싱
import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')
parser.add_argument('-s', '--sub', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("총합 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("총곱 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))
if args.sub:
    print("총합 %d입니다." % functools.reduce(lambda x, y: x - y, args.sub))