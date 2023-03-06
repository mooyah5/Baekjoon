# 소수 찾기
# Silver 5

# 주어진 N개의 수 중 소수가 몇개냐

# 입력
# 첫 줄에 N (주어질 수의 개수)
# N개의 수가 공백을 구분하여 주어짐

# 출력
# 소수의 개수 (약수가 자기자신과 1뿐인 수)

N = int(input())
arr = list(map(int, input().split()))
ans = 0             # 소수의 개수
for a in arr:       # 주어진 수를 하나씩 순회
    decimals = []   # 각 수의 약수를 담을 배열
    for i in range(1, a+1):
        if a % i == 0:          # 0으로 나누어떨어지면 약수이므로 담기
            decimals.append(i)
    if len(decimals) == 2:      # 약수의 개수가 2개면 소수
        ans += 1
print(ans)
