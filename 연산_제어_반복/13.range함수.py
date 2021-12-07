# range(시작,끝값,증가치)
# 시작값 <= 리스트 < 끝값
# r = range(1, 5, 1) # 1 <= list < 5 [1, 2, 3, 4]
# print(list(r))
# r = range(1, 5, 2) # 1 <= list < 5 [1, 3]
# print(list(r))
# r = range(1, 5) # 1 <= list < 5 [1, 2, 3, 4]
# print(list(r))
# r = range(5) # 0 <= list < 5 [0, 1, 2, 3, 4]
# print(list(r))

# for n in range(1, 5):
#     if n == 3:
#         continue
#         # break
#     print(n)

# 1 ~ 10까지의 숫자중 3의 배수를 제외하고 출력하시요.
# for n in range(1, 11):
#     if n % 3 == 0:
#         continue
#     print(n)