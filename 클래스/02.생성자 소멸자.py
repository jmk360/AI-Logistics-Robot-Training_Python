import sys

class Test: 
    def __init__(self, a=0, b=0):
        print('init call')
        self.a = a
        self.b = b

    def __del__(self): #소멸자함수(객체 소멸전 호출되는 함수)
        print('del call')

    def setData(self,a,b):
        self.a = a
        self.b = b
    def showData(self):
        print( self.a, self.b )

def fn():
    obj = Test(100, 200)
    obj.showData()
    return obj

rst = fn() # 이렇게 하면 객체는 소멸하지 않는다.
# 왜냐하면 함수가 리턴하면 eax라는 임시 레지스터에 저장을하고 스택영역에 지역변수가 소멸하고, eax에 저당된 값이 fn() 이 자리로 리턴된다.
print('rst id', id(rst))
rst.setData(11,22) # rst.setData(rst, 11, 22)
rst.showData() # rst.showData(rst)
print('hello')
# 결론: 파이썬의 메모리 자동관리는 참조계수기법

obj = Test(100,200) #obj.__init__(obj,100,200)
print(sys.getrefcount(obj) - 1) # 레퍼런스 카운트를 확인할 수 있다. # sys.getrefcount()는 수를 세기위해서 자체적을 한번더 참조를하기때문에 1을 빼야한다.
my = obj
print(sys.getrefcount(obj) - 1)

print( id(my), id(obj))
obj.showData()
obj = 'korea'
my.setData(11,22) #my.setData(my, 11,22)
my.showData() #my.showData(my)
print('hello')