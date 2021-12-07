# generator -> 굉장히 많이 나오고, 이해하는 것이 매우 중요하다
# generator 만드는 방법 : 1. comprehension 괄호 2. yield

import sys

myList = [ n * 10 for n in range(1, 1000) ] # 이거는 tuple이 아니고 generator 이다
print(myList)
print(sys.getsizeof(myList)) # 해당 객체가 메모리에 얼만큼 차지하는지 알 수 있음 (바이트 단위 인듯 싶다.)
print('--------------')
myG = ( n * 10 for n in range(1, 6) ) # 이거는 tuple이 아니고 generator 이다
# my = list(myG) # [ next(myG), next(myG), ...]
# print(my)
# print(next(myG)) # StopIteration error 가 발생한다. -> 위에서 리스트 만들때 next를 다 호출 했기 때문에...
print(myG)
print(sys.getsizeof(myG)) # generator는 사이즈(메모리) 변화가 없다.
#
# for n in myG: # n = next(myG) 이거를 반복한다. stopIteration error 가 발생할때까지...
#     print(n)
print(next(myG))
print(next(myG))
print(next(myG))
print(next(myG))
print(next(myG))
# print(next(myG)) # stopIteration error 발생