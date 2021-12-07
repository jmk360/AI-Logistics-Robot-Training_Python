# 일급함수도 데이터분석, 인공지능쪽에서 중요하다.

# 일급함수(함수의주소): 할당, 리턴, 인자, 함수 안에 함수
def fn():
    print('fn call')

def fn1(aa):
    aa()

def rFn():
    return fn

rst = rFn()
rst()
fn1(fn)

fn() # function call
print(id(fn))
my = fn # shallow copy (얕은 복사)
my() # function call