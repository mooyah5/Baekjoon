import sys

def binary_search(Narr,m):
    s, e = 0, len(Narr)-1

    while s <= e:
        mid = (s+e)//2
        if Narr[mid] == m:
            return 1
        elif m < mid:
            e = mid-1
        else:
            s = mid+1
    return 0

N = int(sys.stdin.readline())
Narr = list(map(int, sys.stdin.readline().split()))
Narr.sort()

M = int(sys.stdin.readline())
Marr = list(map(int, sys.stdin.readline().split()))

for m in Marr:
    print(binary_search(Narr,m))


