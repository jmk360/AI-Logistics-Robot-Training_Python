s1 = '   abc   '
s2 = '###abc---'
s3 = 'abc def ghi'
s4 = '000-1111-2222'
s5 = 'i like python like program'
# 문자열 좌우 화이트스페이스(' ', \n, \r) 제거
print(s1.strip())
print(s2.strip('-#')) # 굉장히 많이 사용되는 함수

# 화이트 스페이스 기준 분리
print(s3.split()) # document 단축키 : ctrl + q # 굉장히 많이 사용되는 함수
print(s4.split('-', 1)) # 2번째 인자는 몇번 자를 건지를 지정 # 1번 자름
print(s4.split('-', 2)) # 2번 자름

# 대체
print(s5.replace('like', 'love', 1))