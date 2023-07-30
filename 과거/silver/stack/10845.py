# 큐
# Silver 4

# 명령은 총 여섯 가지

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
from sys import stdin

N = int(stdin.readline())    # 명령의 수
q = []
for i in range(N):
    S = stdin.readline()
    if S[1] == 'u':
        q.append(int(S[5:]))
    elif S[1] == 'o':
        print(q.pop(0)) if q else print(-1)
    elif S[0] == 's':
        print(len(q))
    elif S[0] == 'e':
        print(0) if q else print(1)
    elif S[0] == 'f':
        print(q[0]) if q else print(-1)
    elif S[0] == 'b':
        print(q[-1]) if q else print(-1)
