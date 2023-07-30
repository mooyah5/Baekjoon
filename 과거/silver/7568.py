# 덩치

# "더 크다" 의 기준
# A, B의 덩치가 (x, y), (p, q)라면, x>p and y>q 이어야 A > B 이다.
# 등수는 같은 수준의 사람끼리는 동등하며, 그 수만큼 뒤쳐짐 (ex. 1, 2, 2, 2, 5)

N = int(input())
arr = [[i] + list(map(int, input().split())) + [0] for i in range(N)]
arr = sorted(arr, key=lambda x: (-x[1], -x[2]))

print(arr)
j = 1
tmp = 0
for i in range(N - 1):
    if arr[i][1] > arr[i + 1][1] and arr[i][2] > arr[i + 1][2]:
        print(i, "big", j)
        arr[i][3] = [j + tmp]
        j += 1
        tmp += 1
    else:
        print(i, "same", j)
        if tmp == 0:
            tmp = j
        else:
            tmp += 1
        arr[i][3] = [j]
print(tmp)
