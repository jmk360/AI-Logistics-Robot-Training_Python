def fn1():
    return 10,20

def shape(r, h, w):
    return r**2*3.14, h*w

def fn2(a, b):
    print(a, b)

def fn3(a = 10, b = 20):
    print(a, b)

fn3()
fn3(100)
fn3(100, 200)
fn3(b=1000)

# fn2(11,22)
# fn2(b=100, a=200) # 함수를 호출 할때 인자를 명시해서 호출 할 수 있다.


# rst = shape(3, 10, 20)
# print(rst)

# rst = fn1()
# print(rst)
#
# a, b = fn1()
# print(a, b)