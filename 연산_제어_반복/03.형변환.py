n = '22'
n = int(n)
print(n, type(n))
print('--------------------')
a = 10
a = str(a)
print(a, type(a))
print('--------------------')
b = '3.14'
b = float(b)
print(b, type(b))
print('--------------------')
c = (10, 20, 30)
c = list(c)
print(c, type(c))
print('--------------------')
d = [10, 20, 30]
d = tuple(d)
print(d, type(d))
print('--------------------')
e = {'aa':10, 'bb':20, 'cc':30}
e = list(e)
print(e, type(e))
print('--------------------')
f = [10, 20, 30]
f = enumerate(f)
f = dict(f)
print(f, type(f))
print('--------------------')

# 정말 많이 사용하는 것 : zip -> 데이터 분석쪽에서 아주 많이 나온다. 이걸 알면 상당히 유용하다.
g = ['a', 'b', 'c']
h = [11, 22, 33]
z = zip(g, h)
print(z)
print(dict(z))
print(list(z))