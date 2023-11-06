# 암호 처리

# 입력암호화
## getpass 모듈을 사용해 입력시 미표시되도록 처리
""" import getpass 

# pw = input("Password: ") # 보임
pw = getpass.getpass("P123assword: ") # 안보임
print(pw) """


# 해시함수
""" 입력 데이터의 크기나 형식에 상관없이
항상 일정한 길이의 고유한 크기와 형태로 반환되는 함수 """

# 해시알고리즘
# sha256
## : 암호학 및 데이터 무결성 확인과 같은 보안 관련 작업에서 사용, 
## sha-2(2세대)계열, 256bit(32byte) 해시값 생성

## hashlib 모듈의 sha256 알고리즘 활용해 구성
""" import hashlib

hl = hashlib.sha256()
# target = "hello"
# target = "hi"
# target = "world"
# target = "python"
target = "media"

hl.update(target.encode("utf-8"))
print(hl.hexdigest()) """

# keccak256
## : sha-3(3세대) keccak 해시 함수 알고리즘을 활용, 
## 256bit(32byte) 해시값 생성

# 모듈설치 pip install pycryptodome

""" import Crypto.Hash.keccak as kek

target = "media"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest()) """


# 활용
## getpass와 hashlib를 활용해 패스워드 암호화
""" import getpass
import hashlib

pw = getpass.getpass("Pass : ")
hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest()) """

""" import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass : ')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
        
    else: 
        return True
    
if pwInsert():
    pw = input('new pass : ')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
        
else:
    print("not allow password") """
    
    
# 시스템정보 확인
## platform 모듈을 확인해 현재 시스템의 정보를 확인
""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()  
print(ps) """


# 웹페이지 읽기
## urllib 모듈, requests 모듈 활용해 웹페이지 정보 읽기
## 3가지 모드가 있다

# 1모드
""" import urllib.request as ur

url = 'https://www.google.com'

res = ur.urlopen(url)
web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
print(web) """

# 2모드
""" import http.client as hc

url = 'www.google.com'

conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulcl.html", "wb") as fp:
    fp.write(r.read())

conn.close()

print(r) """

# 3모드
"""  import requests

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)"""
    

# 멀티스레드
## threading 모듈을 이용해 멀티스레드를 구현

# 싱글스레드
""" import time
start = time.time()

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

for i in range(3) :
    counter(f"num{i}")

end = time.time() 

print("single end", end - start) """

# 멀티스레드
""" import threading as td
import time

start = time.time()

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end = time.time() 

print("multi end", end - start) """


# 멀티프로세싱
## multiprocessing 모듈을 이용해 분산 처리를 지원, 병렬처리
""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num",))
process3 = mp.Process(target=counter, args=("3num",))

start = time.time()

process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()

end = time.time() 
print("prioc-end", end - start) """


# main 실행
## “__main__” 을 이용해 해당 코드 블록을 직접 실행 하게끔 구성
def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    # run()
    main()