# 덱

# 정수를 저장하는 덱(deque)를 구현한 다음,
# 입력 명령 처리 프로그램 작성
'''
8가지 명령
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

# 첫째줄 명령의 수 n
# 둘째줄부터 명령이 하나씩 (정수는 100000이하)
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    s = input()
    if s[-1].isdecimal():
        pushh, num = s.split()
        if pushh == 'push_front':
            d.appendleft(num)
        elif pushh == 'push_back':
            d.append(num)
    elif s == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif s == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif s == 'size':
        print(len(d))
    elif s == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif s == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)