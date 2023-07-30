# 동전 0 (그리디)
# S4
# 20230514

# 문제
# 준규가 가진 동전의 종류는 N가지
# 각 동전들을 활용해서 가치의 합을 K로 만들 때
# 필요 동전 개수를 최소로 하고 싶다.
# K원 만드는 데 필요한 동전개수 최솟값을 출력하자

# 입력
# 첫째 줄에 동전 종류 N, 목표 금액 K
# 둘째줄부터 N줄에 동전 가치가 오름차순으로 주어짐

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
cnt = 0
for i in range(N):
    if K <= 0:
        break
    while arr[i] <= K and K > 0:
        if arr[i] > K or K <= 0:
            break
        K -= arr[i]
        cnt += 1
print(cnt)
