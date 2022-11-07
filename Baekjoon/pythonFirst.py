# 컨트롤+F5
# print("Hello world")
# print("Mary's cosmetics")

# print('"C:\Windows"')
# print("안녕하세요.\n만나서\t\t반갑습니다.")
# print ("오늘은", "일요일")
# print(5/3)

# 삼성전자 = 50000
# 평가금액 = 삼성전자*10
# print(평가금액)

# 시가총액 = '298'+'조'
# 현재가 = "50000"+'원'
# PER = 15.79

# s = "hello"
# t = "python"

# print(s+"! "+t)

# a = "132"
# print(type(a))


# letters = 'python'
# print(letters[0],letters[2])

# license_plate = "24가 2210"
# print(license_plate[::-1])

# string = "PYTHON"
# print(string[::-1])

# phone_number = "010-1111-2222"
# print(phone_number.replace('-',' '))

# print('-'*80)

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름:%s 나이:%d \n이름:%s 나이:%d."  % (name1,age1,name2,age2))

# 상장주식수 = "5,969,782,550"
# print(int(상장주식수.replace(',','')))

# data = "   삼성전자    "
# print(data.strip())

# ticker = "btc_krw"
# print(ticker.upper())

# hello = 'hello'
# print(hello.capitalize())

# file_name = "보고서.xlsx"
# print(file_name.endswith('xlsx'))

# print(file_name.endswith(('xlsx','xls')))

# file_name = "2020_보고서.xlsx"
# print(file_name.startswith('2020'))

# a = "hello_world"
# print(a.split('_'))

# date = "2020-05-01"
# print(date.split('-'))

# data = "039490     "
# print(data.rstrip())

# movie_rank=['닥터 스트레인지','스플릿','럭키']
# movie_rank.append("배트맨")
# movie_rank.insert(1,"슈퍼맨")
# del movie_rank[3]
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]

# langs = lang1+lang2
# print(langs)

# nums = [1, 2, 3, 4, 5, 6, 7]
# print('max: ',max(nums))
# print('min: ', min(nums))

# nums = [1,2,3,4,5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1,2,3,4,5]
# print(sum(nums)/len(nums))

# price = ['20180728', 100, 130, 140, 150, 160, 170]

# print(price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0::2])
# print(interest[0],interest[2])

# my_variable = ()
# movie_rank = ('닥터 스트레인지','스플릿','럭키')
# a = (1,)
# print(type(a))

# t = ('a a', 'b', 'c')
# tList = list(t)
# tList[0]="A A"
# t=tuple(tList)
# print(t)

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# print(list(interest))
# print(tuple(interest))

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# print(tuple(range(2,99,2)))

# a, b, *c = (0, 1, 2, 3, 4, 5)
# print(c)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *valid_score ,b= scores
# print(valid_score)

# temp={}
# print(type(temp))

# dict = {'메로나':1000, '폴라포':1200, '빵빠레': 1800}
# print(dict)
# dict ['죠스바']=1200
# dict ['월드콘']=1500
# print(dict)

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# ice['메로나']=1300
# del ice['메로나']
# print(ice)

# from unittest import result


# inventory = {'메로나':(300,20), '비비빅':(400,3),'죠스바':(250,100)}
# print(inventory['메로나'][0], '원')

# inventory['월드콘']=(500,7)
# print(inventory)

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(list(icecream.keys()))

# print(list(icecream.values()))

# print(sum(icecream.values()))

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}

# icecream.update(new_product)
# print(icecream)


# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)

# result = zip(keys,vals)
# print(dict(result)) 

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]

# close_table = dict(zip(date, close_price))
# print(close_table)

# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")

# a = input()
# print(a*2)

# a = int(input("숫자 입력"))
# if a%2==0:
#     print("짝수")

# else:
#     print("홀수")

# a = int(input("입력값: "))
# if a+20>255:
#     print(255)
# else:
#     print(a+20)

# a = input("현재시간: ")
# na = a.split(":")
# print(na)
# if(na[1]=='00'):
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다")

# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은?")
# if a in fruit:
#     print("정답입니다.")


# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("제가 좋아하는 계절은?")
# if a in fruit.keys():
#     print("정답입니다.")



# a= input("")
# if a.islower()==True:
#     print(a.upper())
# else:
#     print(a.lower())

# a = int(input("score: "))
# if(a>=81):
#     print("A")
# elif(81>a>=61):
#     print("B")
# else:
#     print("E")

# list = []
# n1 = int(input("input number1: "))
# list.append(n1)
# n2 = int(input("input number2: "))
# list.append(n2)
# n3 = int(input("input number3: "))
# list.append(n3)
# print(max(list))

# n = input("우편번호: ")
# g = int(n[2:3])
# if(0<=g<3):
#     print("강북구")
# elif(3<=g<6):
#     print("도봉구")
# elif(6<=g<=9):
#     print("노원구")

# n = input("주민등록번호: ")
# p = n[8:10]
# if(p in ['00','01','02']):
#     print("서울입니다.")
# elif(p in ['09','10','11']):
#     print("부산입니다.")

# import requests 

# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# o = int(list(btc.values())[0])
# c = int(list(btc.values())[1])
# mi = int(list(btc.values())[2])
# ma =int( list(btc.values())[3])

# b = ma - mi
# if(o+b>ma):
#     print("상승장")
# else:
#     print("하락장")

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# for 변수 in ["A", "B", "C"]:
#   print(변수)

# for 변수 in ["10","20","30"]:
#     print("변수 = ",변수)

# for 변수 in ["10","20","30"]:
#     print(변수)
#     print("------")

# 리스트 = [100, 200, 300]
# for s in 리스트:
#     print(s+10)

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for v in 리스트:
#     print(len(v))

# 리스트 = ['dog', 'cat', 'parrot']
# for v in 리스트:
#     print(v, len(v))

# for v in 리스트:
#     print(v[0:1])

# 리스트 = [1, 2, 3]
# for v in 리스트:
#     print(3,"x",v)

# 리스트 = ["가", "나", "다", "라"]
# # for v in 리스트:
# #     if(v=="가"):
# #         continue
# #     else:
# #         print(v)


# # for v in 리스트[1:]:
# #     print(v)

# # for v in 리스트[0::2]:
# #     print(v)

# for v in 리스트[::-1]:
#     print(v)

# 리스트 = [3, -20, -3, 44]
# for v in 리스트:
#     if(v<0):
#         print(v)

# 리스트 = [3, 100, 23, 44]
# for v in 리스트:
#     if(v%3==0):
#         print(v)





# 리스트 = [13, 21, 12, 14, 30, 18]
# for v in 리스트:
#     if(v<20):
#         if(v%3==0):
#             print(v)

# 리스트 = ["I", "study", "python", "language", "!"]
# for v in 리스트:
#     if(len(v)>=3):
#         print(v)

# 리스트 = ["A", "b", "c", "D"]
# for v in 리스트:
#     if(v.isupper()==True):
#         print(v)



# 리스트 = ['dog', 'cat', 'parrot']
# for v in 리스트:
#     print(v[0:1].upper()+v[1:])

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for v in 리스트:
#     s = v.split('.')
#     print(s[0])

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for v in 리스트:
#     s = v.split('.')
#     if(s[1]=='h'):
#         print(v)

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for v in 리스트:
#     s = v.split('.')
#     if(s[1]=='h'):
#         print(v)
#     elif(s[1]=='c'):
#         print(v)
#     else:
#         continue

# for v in range(0,100):
#     print(v)

# for v in range(2002,2050,4):
#     print(v)

# for v in range(3,31,3):
#     print(v)

# for v in range(99,0,-1):
#     print(v)

# for v in range(0,10):
#     print(v/10)

# for v in range(1,10,2):
#     print(3,'x',v,'=',3*v)



# 파이썬 문제 복습 300제
# https://wikidocs.net/7033 