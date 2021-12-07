# 제너레이터 만든는 법
# 1. comprehension 이용
# 2. 함수이용(yield)

# 제너레이터의 장점은 메모리를 점유하지 않는다.

def fn(): # 함수에 yield 가 들어있으면 제너레어터 함수이다.
    yield 10
    yield 20
    yield 30

def fn1(dt):
    for n in dt:
        yield n+10

def yaksu(num):
    # return [n for n in range(1, num+1) if num % n == 0] # return (n for n in range(1, num+1) if num % n == 0) # 이렇게 해도 제너레이터이다.
    for n in range(1, num+1):
        if num % n == 0:
            yield n

g = yaksu(1000000)
for n in g:
    print(n)

g = fn1([1, 2, 3])
print(g)
for n in g:
    print(n)
# print(next(g))
# print(next(g))

g = fn()
print(g)
print(next(g))
print(next(g))
print(next(g))
# # print(next(g)) # StopIteration error 발생