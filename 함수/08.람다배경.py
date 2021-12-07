#함수기반설계원칙( clean code ) :
# 신규개발(20%미만, 80%: 유지보수) 코드라인수, if문, 명령규칙

# 코드라인수, if문 은 작을 수록 좋다.

# 1. SRP(단일책임): 함수는 하나의 기능만..
# 2. Open-Closed:함수안에서 변동가능한 부분을 함수주소를 이용해 분리
# Gof패턴( 인터페이스기반 )
data1 = [10, 20, 30, 25]
data2 = [(10,20), (70, 15), (40,50)] # (국어, 영어)
data3 = [{'kor':10, 'eng':20},
         {'kor':70, 'eng':15},
         {'kor':40, 'eng':50}
         ]
def mymax(dt):
    mx = dt[0] # {'kor':10, 'eng':20}
    for n in dt[1:]: # n {'kor':70, 'eng':15}
        # if n > mx:
        #     mx = n
        if n['eng'] > mx['eng']:
            mx = n
    return mx

m = mymax(data3)
print(m, m['eng'])
# m = mymax(data2)
# print(m, m[0])
# m = mymax(data1)
# print(m)