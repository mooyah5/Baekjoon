from tkinter import E


N = int(input())
# 가장 작은 생성자 구하기
# N은 생성자의 분해합 (M + M의 각 자리수의 합)
if N <= 10:
    print(N)
else:
    for i in range(1, N+1):
        a = str(i)
        ssum = 0
        for j in a:
            ssum += int(j)
        ssum += int(a)
        if ssum == N:
            print(int(a))
            break
    else:
        print(0)
