# 분해합
# Bronze 2

n = int(input())
minAns = 0
for i in range(n, 0, -1):
    s = str(i)
    sum_ = 0
    for j in range(len(s)):
        sum_ += int(s[j])
    if i + sum_ == n:
        minAns = i
print(minAns)
