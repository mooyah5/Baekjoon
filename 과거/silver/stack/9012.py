# # 괄호

# N = int(input())

# for _ in range(N):
#     S = input()
#     q = []
#     for s in S:
#         if s == '(':                # 여는 괄호면
#             q.append(s)             # 스택에 넣는다.
#         elif s == ')' and len(q) == 0:  # 닫는 괄호 + 스택이 비었으면
#             q.append('no')              # 스택 안에 no를 넣고
#             print('NO')                 # NO 출력 후 for 문 탈출
#             break
#         elif s == ')':              # 스택에 값이 있는데 닫는 괄호면
#             q.pop(-1)               # 이전에 넣어놨던 여는 괄호 하나를 제거

#     if len(q) == 0:                 # 스택에 남은 게 없으면 정상괄호이므로
#         print('YES')                # YES 출력
#     elif 'no' in q:                 # 스택에 no가 있으면 아까 NO출력 했으니까 패스 (닫는괄호가 더 많음)
#         pass
#     else:                           # 스택에 남은 게 있으면 여는 괄호가 남은 것이므로
#         print('NO')                 # NO 출력


# 2023-03-04 재도전

n = int(input())
for i in range(n):
    S = input()
    ans = 0
    answer = "YES"
    for s in S:
        if s == '(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            answer = "NO"
            break
    if answer == "NO" or ans != 0:
        print("NO")
    else:
        print("YES")
