# 다른언어
'''
int n = 1;
switch(n)
{
    case 1:
        ....
        break;
    case 2:
        ....
        break;
    default:
        ....
        break;
}
'''
def fn1():
    print('fn1 call')

def fn2():
    print('fn2 call')

def dFn():
    print('default Fn')

menu = {1:fn1, 2:fn2} # 파이썬의 switch문은 딕셔너리로 처리한다.
menu[1]() # 인덱스를 통해서 함수 호출
menu.get(4, dFn)()

myd = {'aa':10, 'bb':20}
print(myd['aa']) # 없는 키를 요청하면 keyerror가 발생
print(myd.get('cc', 1000)) # 없는 키를 요청하면 2번째 인자인 defaul값이 리턴한다.