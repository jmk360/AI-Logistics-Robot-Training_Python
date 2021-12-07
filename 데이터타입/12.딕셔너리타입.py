# 딕셔너리 : {키:값, 키:값 ...}
d = {'aa':10, 'bb':20, 'cc':30}
d['aa'] = 100 # 키가 있으면 수정
d['dd'] = 200 # 키가 없으면 추가

print(d)
print(type(d))
print(d['aa'])
print(d['cc'])

d.pop('aa')
print(d)

print(d.get('ff', 1000)) # d['aa'] 이거랑은 같은 것 같지만 조금 다른다. # 키가 없으면 2번째 인자 디폴트값을 리턴한다.
# 키가 없으면 None을 리턴
print(d.get('ff'))

print(d.keys())
print(d.values())
print(d.items())