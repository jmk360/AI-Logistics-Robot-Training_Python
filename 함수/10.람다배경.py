data1 = [10, 20, 30, 25]
data2 = [(10,20), (70, 15), (40,50)] # (국어, 영어)
data3 = [{'kor':10, 'eng':20},
         {'kor':70, 'eng':15},
         {'kor':40, 'eng':50}
         ]
def fn1(v):
    return v

def fn2(v):
    return v[0]

def fn3(v):
    return v['eng']

def mymax(dt, key):
    mx = dt[0] # {'kor':10, 'eng':20}
    for n in dt[1:]: # n {'kor':70, 'eng':15}
        if key(n) > key(mx):
            mx = n
    return mx

m = mymax(data3, fn3)
print(m)

m = mymax(data2, fn2)
print(m)

m = mymax(data1, fn1)
print(m)

# m = mymax(data3)
# print(m, m['eng'])
# m = mymax(data2)
# print(m, m[0])
# m = mymax(data1)
# print(m)