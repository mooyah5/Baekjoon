# 도키도키 간식드리미
# Silver 3

n = int(input())
lst = list(map(int, input().split()))
stack = []
rank = 0
for l in lst:
    if l == rank + 1:
        rank += 1
    else:
        stack.append(l)
if sorted(stack, reverse=True) == stack:
    print("Nice")
else:
    print("Sad")
# if stack == (sorted(stack))
