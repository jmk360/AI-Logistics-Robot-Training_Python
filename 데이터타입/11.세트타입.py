# set 은 순서가 없다 -> 인덱싱, 슬라이싱 사용 불가능
s = {10, 20, 20, 20, 30, 40, 50}
s.add(100)
s.remove(30)
print(s)
print(type(s))
# print(s[0]) # 에러 나옴
# 집합, 중복데이터 제거

s1 = {10, 20, 30}
s2 = {20, 30, 40, 50}

# 교집합
print(s1 & s2)
print(s1.intersection((s2)))
# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 대칭차집합 : 합집합 - 교집합
print(s1^s2)