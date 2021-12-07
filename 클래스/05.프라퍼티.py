class Calender:
    def __init__(self):
        self.month = 0

    @property
    def Month(self):
        print('get call')
        return self.month

    @Month.setter
    def Month(self, month):
        if month < 1 or month > 12:
            print('wrong month')
        else:
            self.month = month

cal = Calender()
cal.Month = 12
print(cal.Month)