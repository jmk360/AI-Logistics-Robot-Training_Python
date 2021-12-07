# __name__ == '__main__'
# __doc__ = None

g = 10

def fn():
    g = 100
    print('지역변수', locals())

fn()
print('g=', g)
print(__file__)
print(globals()) # 전역변수 목록을 보여준다.