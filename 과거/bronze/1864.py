# 문어 숫자
# Bronze 2

arr = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']
arr2 = [0, 1, 2, 3, 4, 5, 6, 7, -1]

while True:
    S = input()
    if S == '#':
        break

    n = ''
    for s in S:
        n += str(arr.index(s))

    ans = 0
    for i in range(len(n)):
        ans += arr2[int(n[i])] * 8**(len(n)-1-i)
    print(ans)
