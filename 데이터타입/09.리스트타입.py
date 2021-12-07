myList = [10, 20, 30, 40, 50]
# print(myList)
# print(type(myList))
# print(myList[-1])
# print(myList[0])
# print(myList[1:4]) # 주석 단축키 : ctrl + /

# 추가
myList.append(100)
myList.append(200)
myList.insert(1, 1000)

# 삭제
myList.remove(30)
myList.pop(0)
myList.pop()

print(myList)
print(myList.index(20))
print(myList.count(10))
print(len(myList))
s = 'abc'
print(len(s))

# 수정
myList[0] = 11