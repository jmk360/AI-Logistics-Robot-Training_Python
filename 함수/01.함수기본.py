def fn1():
    print('hello')
    print('python')

def hap(a, b): # 아규먼트, 인자, signature
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return None

# 반지름을 인자(입력)로 받아 원의 면적을 반환하는 함수를 만드시요
def circleArea(r): # circleArea
    return 3.14 * r ** 2

# print(circleArea(3))

# 연도를 인자로 받아 '윤년' 또는 '윤년아님' 을 반환하는 함수를 만드시요
def yun(year):
    return '윤년' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '윤년아님'

# 연도를 인자로 받아 띠를 반환하는 함수를 만드시요.
def get_dee(year):
    return ["원숭이", "닭", "개", "돼지","쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", ][ year%12 ]

# print(get_dee(1997))

# 반지름과 높이를 인자로받아 원기둥의 부피를 반환하는 함수를 만드시요
def cylinder_volume(r, h):
    return h * 3.14 * r ** 2

# 반지름과 높이를 인자로받아 원뿔의 부피를 반환하는 함수를 만드시요
def cone_volume(r, h):
    return (h * 3.14 * r ** 2) / 3

# rst = hap(10, 20)
# rst = hap(2.3, 2.2)
# rst = hap('aaa', 'bbb')
# print(rst)
# fn1()
# fn1()
# fn1()