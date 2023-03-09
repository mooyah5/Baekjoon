# 윷놀이
# Bronze 3

# 배 0 와 등 1
rule = ['E', 'A', 'B', 'C', 'D']
for tc in range(3):
    arr = list(map(int, input().split()))
    sumarr = arr.count(0)
    print(rule[sumarr])
