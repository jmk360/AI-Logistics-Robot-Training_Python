# 1. 키와 몸무게를 입력받아 비만도를 구하고 결과를 출력하시요
# 표준체중(kg)=(신장(cm)-100)×0.85
# 비만도(%)=현재체중/표준체중(%)×100
# 비만도가90%이하
# 저체중,
# 90초과~110%
# 정상,
# 110초과~120%
# 과체중,
# 120%초과
# 비만
# sol)
# h, w = map(lambda x:float(x), input('키 몸무게 입력: ').split())
# kg = (h - 100)*0.85
# bb = w / kg * 100
# if bb <= 90:
#     print('저체중')
# elif 90 < bb <= 110:
#     print('정상')
# elif 110 < bb <= 120:
#     print('과제중')
# else:
#     print('비만')

# 2. 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# sol)
# dd = {'달러':1168, '엔':1.096, '유로':1268, '위안':171}
# a, b = input('입력: ').split()
# print(int(a) * dd.get(b), '원')

# 3. 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# sol)
# dd = {'011':'SKT', '016':'KT', '019':'LGU', '010':'알수없음'}
# num = input('>> 휴대전화 번호 입력: ')
# print('당신은 {} 사용자입니다.'.format(dd.get(num[:3])))

# 4. 구구단을 아래와 같이 출력하시요
# 1x1 = 1  2x1=2   3x1=3
# …
# 1x9 = 9  2x9=18  3x9=27
# 4단 	   5단	   6단

# 7단	   8단	   9단
# sol)
# for i in range(1,10,3):
#     for j in range(1,10):
#         print(f'{i}x{j}={i*j}\t{i+1}x{j}={(i+1)*j}\t{i+2}x{j}={(i+2)*j}')
#     print('-'*50)

# 5. 아래 표를 stock 이름의 딕셔너리로 표현하라.
# 시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 
# 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# sol)
# stock = {'시가':[100, 200], '종가':[200,210]}
# print(stock)

# 6 .콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# sol)
# def convert_int(ss):
#     return int(ss.replace(',',''))
# print(convert_int("1,234,567"))

# 7. 하나의 정수를 인자로 받아 해당 소수를 제너레이터로 반환하는 함수를 만드시요
# sol)
# def gen(n):
#     for i in range(2,n+1):
#         tmp = True
#         for j in range(2,i):
#             if i % j == 0:
#                 tmp = False
#                 break
#         if tmp:
#             yield i
# print(list(gen(50)))

# 8. 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# sol)
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# areum = Human('아름', 25, "여자")
# print(areum.__dict__)

# 9. 로또를 구현하시요
# 입력: 6 자리 중복되지않게

# Ex : (정답 1 6 8 13 24 35)
# Ex : 입력 : 1 6 8 11 22 33
# Ex : 1,6,8 3개가 맞았습니다.
# sol)
# from random import randint
# answer = []
# for i in range(6):
#     while True:
#         a = randint(1,45)
#         if a not in answer:
#             answer.append(a)
#             break
# print('정답:',answer)
# qq = list(map(lambda x:int(x), input('입력: ').split()))

# bb = set(answer) & set(qq)
# print(f'{bb} {len(bb)}개 맞았습니다.')