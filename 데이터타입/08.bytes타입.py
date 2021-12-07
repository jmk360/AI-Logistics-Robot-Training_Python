# 통신 (octet 1byte) -> 통신은 byte 기준이다.
# bytes타입은 통신에서 많이(주로) 사용된다. -> 입사면접에서 물어 볼 수 있다.
# python ---- write(send) ----> 장치, 호스트
# str ---> bytes로 변환
# python < ---- read(recv) ---- 장치, 호스트
# bytes --> str 로 변환

a = 'hello' # 문자 하나당 2byte # 통신을 하기 위해서는 문자하나당 1byte여야 한다. 즉, str을 bytes로 변환해야 한다.
b = b'abc' # 문자 하나당 1byte # 앞에 b 자 붙은게 byte 타입이다.
print(b, type(b))
print(b[0]) # 아스키값이 나온다.

a = a.encode()
print(a, type(a))

b = b.decode()
print(b, type(b))