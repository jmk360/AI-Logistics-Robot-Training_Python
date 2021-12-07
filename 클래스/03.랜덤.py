import random
for i in range(10):
    rnd = random.randint(1,5) # 1<=n<=5 중 랜덤으로 반환
    print(rnd)

my = [11, 22, 33, 44, 55]
random.shuffle(my)
print(my)