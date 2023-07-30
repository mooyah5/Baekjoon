# B5
# 코딩은 체육과목입니다
# 주어지는 정수의 크기를 4로 나눈 값을 long의 개수로 둔다.
# 나누어 떨어지면(나머지 0) 그대로 출력, 그렇지 않으면 long += 1

N = int(input())
long = N // 4
if N % 4 == 0:
    pass
else:
    long += 1

print(('long ' * long) + 'int')
