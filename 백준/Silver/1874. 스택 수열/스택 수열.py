import collections

N = int(input())
stack = collections.deque()
i = 1  # 1부터 N까지 오름차순으로 넣어줄 값
answer = []  # 정상 답 출력을 위해 '+' 혹은 '-'을 넣어줄 리스트
state = True  # 비정상 답 'NO' 출력을 위해 불가능한 상황일 경우 False로 상태 변경
last = 0
for _ in range(N):
    target = int(input())   # 타겟: 스택에서 꺼낼 수

    while i <= target:      # 스택에 타겟까지 오름차수를 채운다.
        stack.append(i)
        answer.append("+")
        i += 1

    if stack.pop() == target:   # 스택 끝 값이 타겟과 일치하면 꺼내면서 '-' 추가
        answer.append("-")
    else:                       # 스택 끝 값이 타겟과 다르면 불가능 (이미 채워졌기에 타겟보다 작아도 꺼낼 수 없음.)
        state = False
        break

if state == False:
    print("NO")
else:
    for ans in answer:
        print(ans)
