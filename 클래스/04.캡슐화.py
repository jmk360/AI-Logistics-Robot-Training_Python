class Calendar:
    def __init__(self):
        self.month = 0

    def setMonth(self, month):
        if month < 1 or month > 12:
            print('wrong month')
        else:
            self.month = month

    def getMonth(self):
        return self.month

# 멤버데이터 직접 접근시 데이터 무결성을 보장하지 못한다.
# 메소드를 통해 데이터를 R/W : 캡슐화 get, set # -> 클래스 설계의 기본 원칙이다.
cal = Calendar()
# cal.month = 13
cal.setMonth(12)
print(cal.getMonth())