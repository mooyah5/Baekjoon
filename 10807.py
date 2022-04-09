# 개수 세기
# 첫째줄 1 <= n <= 100
# 둘째줄 정수 n개가 공백으로 구분
# 셋째줄 찾으려는 정수 -100 <= v <= 100
# 출력 n개의 정수 중 v의 개수

n = int(input())
arr = list(map(int,input().split()))
v = int(input())
cnt = 0
for a in arr:
    if a == v:
        cnt += 1
print(cnt)