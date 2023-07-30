# 2007년
# B1

# 문제
# 오늘은 2007년 1월 1일 월요일이다. (실제 요일 일치)
# 그렇다면 2007년 x월 y일의 요일은?

## 1. datetime 모듈 사용하기
from datetime import datetime

x, y = map(int, input().split())
basic = datetime(2007, x, y)
print(basic.strftime("%a").upper())

## 2. 노가다
x, y = map(int, input().split())
# 먼 훗날의 나에게 토스
