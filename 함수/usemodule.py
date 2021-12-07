# import mymodule
# import mymodule as m
# from mymodule import circleArea, cylinder_volume
import sys
# python path 를 추가하는 방법 1. 환경변수 추가 2. 코드로 추가 # 일반적으로는 코드(코딩)으로 추가한다.
print(sys.path) # 여기서 출력된 곳이 python path이다. mymodule을 갖다놓으면 다 정상적으로 import 한다.
# sys.path.append(r'C:\mylib') # 파이썬 패스 라이브러리 경로 추가
from mymodule import *
rst = circleArea(3)
print(rst)
rst = cylinder_volume(3, 10)
print(rst)

# rst = m.circleArea(3)
# print(rst)
#
# rst = m.cylinder_volume(3, 10)
# print(rst)

# rst = mymodule.circleArea(3)
# print(rst)
#
# rst = mymodule.cylinder_volume(3, 10)
# print(rst)