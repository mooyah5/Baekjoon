# 230612

import sys

input = sys.stdin.readline
N = int(input())

ans = 0
for i in range(N):
    ans += 1
    if str(i).find("50") > -1:
        ans += 1
print(ans)
