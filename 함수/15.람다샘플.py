data1 = [10,20,30,25]
data2 = ['10','20','30','25']

def mymap(func,dt):
    return [func(n) for n in dt]

# rst = mymap(lambda v:v*10,data1)
rst = mymap(lambda v:int(v), data2)
print(rst)
rst = map(lambda v:v+10, data1) # map은 개별 데이터를 더하고, 빼고, 곱하고, 나누고, 형변환 하는데 보통 쓰인다.
print(rst)
# print(next(rst))
for n in rst:
    print(n)