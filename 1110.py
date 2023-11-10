# 멀티프로세싱
## multiprocessing 모듈을 이용해 분산 처리를 지원, 병렬처리_(복습)
""" import multiprocessing as mp
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

if __name__ == "__main__":
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


# 비동기 처리
## asyncio 모듈을 이용해 비동기 처리를 구현
""" import asyncio
import random as rd
import time

async def tester(name):
    snum = rd.randint(10, 20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
    print(f"end of {name}")

async def main():
    task1 = asyncio.create_task(tester("1test"))
    
    task2 = asyncio.create_task(tester("2test"))
    
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end", end-start)
    
if __name__ == "__main__":
    asyncio.run(main()) """

##비동기처리2
""" import asyncio
import time

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)
        
async def worker2():
    for i in range(1, 4):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(2)
    
async def main():    
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())
    
    print("start task")
    start = time.time()
    await task_1
    await task_2
    end = time.time()
    print("end", end-start)
    
if __name__ == "__main__":
    asyncio.run(main()) """
    
    
# 스케쥴
## sched 모듈을 이용한 스케쥴 실행을 구성
""" import sched
import time

start = time.time()

def tester(name):
    print(f"start-time {time.time()-start}")
    for i in range(3):
        print(f"{name}-{i}")
    
    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run()
    
if __name__ == "__main__":
    run()
    # main()
    print("end")"""
    
    
# 문자열 비교
## diff_match_patch 모듈을 설치해야 합니다.
## pip install diff_match_patch
""" import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, That is a question!"

dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """
    

# 테스트용 데이터 생성 
## Faker 모듈을 설치하여 임의의 데이터를 생성 
## pip install Faker
""" from faker(A) import Faker(B)
import faker(A).Faker(B) 
이런형태의 임포트가 지원되는 애가 있고 
안되는 애 있음
일단 해보고 안되면 프롬 푸를것 """
""" from faker import Faker as fk

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

with open("fktemp.csv", "w", newline='') as f:
    for i in range(30):
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
 
     
# 시스템명령어 사용
## subprocess 모듈을 활용해 시스템 명령어를 실행
""" import subprocess as sp

# res = sp.run(["cmd", "/c", "dir"], capture_output=True)
# res = sp.run(["cmd", "/c", "dir"], capture_output=False)
# res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=True)
res = sp.run(["cmd", "/c", "ipconfig", "/all"], capture_output=False) #실행파일을 넣어도 됨

print(res) """


# 에러처리
## try ~ except 로 처리

""" try :
	구현 코드
except :
	구현 코드중 에러 발생시 실행할 코드 """

""" import traceback as tb

def tester():
    # return 1
    return 1/0

def caller():
    tester()
    
def main():
    try:
        caller()
        
    except ZeroDivisionError:
        print("zde error")
        # 0을 나누어 에러 발생시 처리 여기 주석처리하면 ex에서 처리됨

    except ValueError :
        print("ve error")
	# 유효하지 않는 정수를 입력했을시 처리

    except Exception as ex :
        print("ex error", ex)
	# 모든 예외를 처리할때 처리

    else :
        print("ok")
	# 에러가 없으면

    finally :
        print("end")
	# 해당 함수가 에러가 있든 없든, 완료될때 처리
 
if __name__ == "__main__":
    main() """
    

# HTML
## 태그를 사용하여 웹페이지를 구성하고 마크다운 언어
# 교재 참고


# CSS
## HTML을 효율적으로 꾸미기 위한 구성 파일


# 웹크롤링
## 파싱(Parsing) : HTML을 다운로드하여 가시성을 향상시켜 다루기 쉬운 형태로 만들어
                # 원하는 데이터만을 가져오는 작업
## pip install beautifulsoup4, pip install requests
##import bs4.BeautifulSoup
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

# pres = res_html.find("h1")
pres = res_html.find("h2")
print(pres)
print("\n1---------------------------------\n")
print(pres.get_text().strip())
print("\n2---------------------------------\n")
print(pres.next_element.get_text().strip())

tres = res_html.find("title")
print(tres)
print("\n3---------------------------------\n")
print(tres.get_text().strip())
print("\n4---------------------------------\n")
print(tres.next_element.get_text().strip())

fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())
    
# print(fares)
print("\n5---------------------------------\n")

clres = res_html.findAll(class_ = "doc-title")
print(clres)

print("\n6---------------------------------\n")
clrs = res_html.find(class_ = "head_top")
print(clres)
print(clrs.get_text()) """

#
""" from bs4 import BeautifulSoup as bs
import requests as rq """

""" url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a")

print(item)
print(item.get_text())
print("\n00---------------------------------\n")
print(item.get_text.strip()) """

#
""" url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

# print(item)
print(item.get_text())
goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods.get_text()) """

#
from bs4 import BeautifulSoup as bs
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
    print(c + "\n")

