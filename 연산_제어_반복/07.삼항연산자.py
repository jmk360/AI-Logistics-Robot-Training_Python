# 다른 언어 : 조건? 참인경우 : 거짓인경우
# 참인경우 if 조건 else 거짓

a = -5
rst = 100 if a > 0 else 200
print(rst)

aa = False + 1 # 2
print(aa)
aa = True + 1 # 2
print(aa)

result = [200, 100][a > 0] # False는 0으로 본다. True는 1으로 본다.
print(result)

result = {True:1000, False:2000}[a > 0]
print(result)