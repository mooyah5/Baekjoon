# 색종이
# Silver 5

# 가로세로 크기 100인 정사각형 도화지에
# 가로세로 크기 10인 정사각형 검은 색종이를 붙인다. (겹칠 수 있음)
# 검은색종이 영역 넓이를 출력

N = int(input())    # 색종이 개수
arr = [[0 for _ in range(100)] for _ in range(100)]
for n in range(N):
    a, b = map(int, input().split())  # 색종이 위치
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1
ans = 0
for a in arr:
    ans += sum(a)
print(ans)
