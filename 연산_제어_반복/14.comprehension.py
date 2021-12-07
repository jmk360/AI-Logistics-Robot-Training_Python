my = [n * 10 for n in range(1, 6)]
print(my)

# 각 연봉의 세금 3.3%을 제한 실수령액을 구하시요
# salary = [1000, 2000, 3000, 4000, 5000]
#
# real = [n * (1 - 0.033) for n in salary]
# print(real)

my = [n * 10 for n in range(1, 6) if n <= 3]
print(my)

# 하나의 정수를 입력받아 해당정수의 약수를 구하시요 # [못푼문제]
# number = int(input('정수입력: '))
# myList = [n for n in range(1, number+1) if number % n == 0]
# print(myList)

my = { n * 10 for n in range(1, 6) }
print(my, type(my))

dt = [('aa',10), ('bb', 20), ('cc',30)]
my = {k:v for k,v in dt}
print(my, type(my))