# 연산자 우선 순위 : 산술 > 관계 > 논리
a = 5
# rst = a > 0 and a == 0
# rst = a > 0 or a == 0
# rst = not a > 0
# rst = not 0
# rst = not None
# rst = not ''
# rst = not []
rst = not 'abc' # 100
print(rst)
# False : 0, None, '', [], (), {} -> 이거 꼭 기억
# True : 0이 아닌 정수(실수), 'ab', [10], (10, 20), 특정클래스객체
print('===============')
# 요소 in 복합데이터타입
print('llo' in 'hello korea')
print(10 not in [10, 20, 30])
myd = {'aa':10, 'bb':20, 'cc':30}
print('aa' in myd) # my.keys()
print(10 in myd.values())