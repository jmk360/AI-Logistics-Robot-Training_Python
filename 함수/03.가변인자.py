def fn(*args):
    print(args)

def circles(*rs):
    for r in rs:
        print(r**2*3.14)

def fn2(*args, a = 11, b = 22): # 일반인자는 초기값을 주어야 한다.
    print('args: ', args)
    print('a=',a)
    print('b=',b)

def fn3(**kwargs): # 정의되지않은 인자 -> 되게 많이 나온다.
    print(kwargs)

# r : 반지름, h : 높이
def cylinder(**kwargs):
    return 3.14*kwargs['r']**2*kwargs['h']
print(cylinder(r=3, h=10))

a = 10
b = 3.14
s = 'abc'
# mys = 'a={0} b={1} s={2}'.format(a, b, s)
# mys = 'a={} b={} s={}'.format(a, b, s)
# mys = 'a={} b={} s={}'.format(*(a, b, s))
# mys = 'a={aa} b={bb}'.format(aa=100, bb=200)
mys = 'a={aa} b={bb}'.format(**{'aa':100, 'bb':200}) # 딕셔너리 unpacking
print(mys)

data = [('홍길동', 20), ('이순신', 30)]
for n in data:
    print('이름:{} 나이:{}'.format(*n))

fn3(aa=10, bb=20)
fn3(name='홍길동', age=20)

fn2(10,20,30,a=40,b=50) # 일반 인자가 받게 하려면 반드시 명시해서 주어야 한다.
# print(*values, sep=' ', end='\n',file=sys.stdout)
# print(10,20,30,40, sep='-')
# print('hello',end=' ')
# print( 'korea')

# 함수 호출할때 인자의 개수 제한이 없다.
fn(10,20)
fn(10,20,30,40)
circles(1,2,3,4,5)
fn((1,2,3))
fn(*(1,2,3)) # tuple unpacking
fn(1,2,3)

# my = (10,) #(10+2)
# print( my, type(my))