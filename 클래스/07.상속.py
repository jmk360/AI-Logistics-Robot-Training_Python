# 상속을 하는 이유 : 재사용을 하기 위함

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def setName(self,name):
        self.name = name

class Student(People):
    def __init__(self,name, age, stdNum):
        super().__init__(name,age)
        self.stdNum = stdNum

# class Student:
#     def __init__(self,name, age, stdNum):
#         self.name = name
#         self.age = age
#         self.stdNum = stdNum
#     def setName(self,name):
#         self.name = name
std = Student('홍길동',20, 20210303 )
print(std.name, std.age, std.stdNum)
#std.__init__(std, '홍길동',20, 20210303)