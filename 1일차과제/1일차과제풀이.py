# 1. 반지름과 높이를 입력받아 다음을 구하시요
# 1) 원기둥의 부피
# 2) 원뿔의 부피
# sol)
# from math import pi
# r, h = map(lambda x:int(x), input('>> ').split()) 
# cylinder = pi * r**2 * h 
# cone = cylinder / 3
# print('원기둥의 부피 : {:.2f}'.format(cylinder))
# print('원뿔의 부피 : {:.2f}'.format(cone))

# 2. 하나의 도를 입력받아 화씨값을 구하시요
# sol)
# do = float(input('도를 입력하세요>> '))
# f = do * 1.8 + 32
# print('화씨 : {}'.format(f))

# 3. cm 를 입력받아 인치를 구하시요
# sol)
# cm = int(input("cm>> "))
# inch = cm * 0.393701
# print(inch)

# 4. km 를 입력받아 마일을 구하시요
# sol)
# km = input("km:")
# print(f"{float(km) * 0.621371} mile")

# 5. 2개의 정수를 입력받아 절대값의 합을 구하시요
# sol)
# a, b = map(lambda x:int(x), input('2개 정수입력: ').split())
# sum = abs(a) + abs(b)
# print(sum)

# 6. 생년을 입력받아 나이를 출력하시요
# sol)
# year = int(input('생년: '))
# age = 2021 - year + 1
# print(age)

# 7. 3개의 정수를 입력받아 가장큰값을 구하시요.
# sol)
# a, b, c = map(lambda x:int(x), input('3개정수입력: ').split())
# if a > b and a > c:
#     max = a
# elif b > a and b > c:
#     max = b
# else:
#     max = c
# print('가장 큰 값: {}'.format(max))

# 8. 년도를 입력받아 띠를 구하시요 ( 2021년은 소띠)
# sol)
# symbol = ["원숭이", "닭", "개", "돼지","쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", ]
# year = int(input('년도 입력: '))
# print(symbol[year % 12])

# 9. 년도를 입력받아 윤년 여부를 출력하시요
# sol)
# year = int(input('년도 입력: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('윤년입니다.') 
# else:
#     print('윤년이 아닙니다.')

# 10. 하나의 점수를 읽어 90~100 'A' 80~89 'B' 70~79 'C' 60~69 'D' 나머지 'F'
# 를 딕셔너리를 이용하여 작성하시요
# sol)
# table = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D'}
# score = int(input('점수입력: ')) // 10
# print(table.get(score,'F'))

# 11. 상품가격과 지불액을 입력하여 거스름돈의 갯수를 최소화하도록 거스름돈을 출력하시요
# (거스름돈, 500, 100, 50, 10 원 4가지종류로 한다 )
# 예) 상품가격 2160원 지불액 3000원이면 500원 1개, 100원 3개 50원0개 10원4개 로출력
# sol)
# product, pay = map(lambda x:int(x), input('상품가격 지불액: ').split())
# exchange = pay - product
# n500 = exchange // 500
# n100 = (exchange % 500) // 100
# n50 = ((exchange % 500) % 100) // 50
# n10 = (((exchange % 500) % 100) % 50) // 10
# print('500원 갯수:', n500, '100원 갯수:', n100, '50원 갯수:',n50, '10원 갯수:',n10)