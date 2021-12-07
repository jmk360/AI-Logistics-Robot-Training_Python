# for 변수 in 복합데이터타입:
# 다른언어 for(초기값;판단;증가치)
myS = 'abc'
myT = (10, 20, 30)
myList = [11, 22, 33]
myD = {'aa':10, 'bb':20, 'cc':30}
for n in myS:
    print(n)

for n in myT:
    print(n)

for n in myList:
    print(n)

print('==============')
for n in myD:
    print(n)

for n in myD.values():
    print(n)

for n in myD.items():
    print(n)

for a, b in myD.items():
    print(a, b)