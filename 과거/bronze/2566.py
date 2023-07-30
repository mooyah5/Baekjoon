# 최댓값
# Bronze 3

# 9*9 격자판에 쓰여진 81개의 자연수 or 0
# 최댓값이 몇 행 몇 열에 위치한 수인지

# 입력
# 9개의 숫자가 공백으로 나뉘어 9줄 입력됨

# 출력
# 최댓값
# 행 열

maxN = 0
x, y = 0, 0
for i in range(9):
    a = list(map(int, input().split()))
    if maxN < max(a):
        x, y = i, a.index(max(a))
        maxN = max(a)
print(maxN)
print(x+1, y+1)
