class Test:
    st = 10 # static 변수
    def __init__(self):
        self.a = 0 # instance (반드시 객체생성필요) -> 객체가 생성이 되어야만 메모리에 올라간다.
        self.b = 0 # instance (반드시 객체생성필요)
    def setData(self,a,b): # 인스턴스 함수
        self.a = a
        self.b = b
    def showData(self): # 인스턴스 함수
        print( self.a, self.b )

    @staticmethod
    def stFn(): # static 메소드(인스턴스변수 사용불가)
        print('stFn')

Test.stFn()

print(Test.st)
obj = Test()
print(obj.a, obj.b)
obj1 = Test()

# 생각해 볼만한 코드
# class Sam(object):
#     name = 'Korea'
#     def get_name(self):
#         return self.name

#     def getlnfo(self):
#         self.get_name()

# s1 = Sam()
# s2 = Sam()
# s3 = Sam()

# s3.name = 'japan'
# print(s1.name)
# print(s2.name)
# print(s3.get_name())

# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)