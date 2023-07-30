# Bronze 3
# 노 땡스!

# 3~35 카드중 카드 N개를 받는다.
# 1씩만 차이나는 카드끼리 묶어서
# 그룹별로 가장 작은 수끼리 합하여 출력

N = int(input())    # 카드의 개수
arr = list(map(int, input().split(' ')))
pre = [arr[0]]                  # 이전 카드 확인용 리스트
ans = arr[0]                    # 그룹별 작은 수 더하기
for i in range(1, N):
    if pre[-1] + 1 == arr[i]:   # 이전 카드보다 1 크면 패스
        pass
    else:                       # 이전 카드와 1차이 나지 않으면
        ans += arr[i]           # 다른 그룹 시작이므로 ans에 더함

print(ans)
