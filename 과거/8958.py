
n = int(input())
for i in range(n):
    oxstr = input()
    score = 0
    count = 0
    for i in oxstr:
        if 'O' == i:
            score += 1
            count += score
        else:
            score = 0
    print(count)
