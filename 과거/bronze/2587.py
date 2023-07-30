# 대표값2
# Bronze 2

arr = []
for i in range(5):
    n = int(input())
    arr.append(n)

print(sum(arr)//5)    # 평균
print(sorted(arr)[2])  # 중앙값
