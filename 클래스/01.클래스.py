class Test:
    def __init__(self): # 생성자 함수(객체생성이 완료되면 자동호출)
        print('init...')
        self.a = 0
        self.b = 0

    def setData(self, a, b):
        print('setdata self id', id(self))
        self.a = a
        self.b = b

    def showData(self):
        print('showData self id', id(self))
        print(self.a, self.b)

# obj(Test 클래스객체, 참조변수)
# obj.속성, obj.멤버함수
# 객체 생성 : 멤버데이터의 메모리 할당이 완료된 상태
obj = Test() # 다른언 Test obj = new Test()
print('obj id', id(obj))

# obj.__init__(obj) 파이썬 컴파일러가...
obj.setData(10,20) # obj.setData(obj,10,20)
obj.a = 100
obj.showData() # obj.showData(obj)

obj1 = Test()
# obj1.__init__(obj1)
print('obj1 id', id(obj1))
obj1.setData(100,200) # obj1.setData(obj1, 100, 200)
obj1.showData() # obj1.showData(obj1)

## 동일한 클래스에서 여러개의 객체가 생성된 경우
# 멤버데이터는 별도 (힙) 멤버함수는 코드로 공유
# 그런데 어떻게 각각의 메모리영역에 값을 R/W
# self(해당객체를 shallow )