## 반지름을 키보드로 입력받아 원의 면적을 구사이요.
# < 내 답>
# import math
# r = input('반지름 입력:')
# area = math.pi * float(r)**2
# print('원의 면적 : {}'.format(area))

# <해답>
# r = int(input('반지름:'))
# circleArea = 3.14 * r ** 2
# print(circleArea)

# 문자열: +(문자열 연결), *, % -> 문자열에서 사용할 수 있는 산술 연산자
s = 'abc'
s = s + 'def'
s = s * 3
print(s)
a = 10
b = 3.14
c = 'hello'
mys = 'a=%10d b=%.2f c=%s'%(a, b, c)
mys = f'a={a:10} b={b:.1f} c={c}' # 3.5버전이상부터 추가된 기능-> 많이 사용
print(mys)