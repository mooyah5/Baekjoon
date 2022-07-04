# 분수 찾기

'''
1/1 1/2 1/3 1/4 1/5
2/1 2/2 2/3 2/4
3/1 3/2 3/3
4/1 4/2
5/1
'''
# 지렁이 처럼 지그재그 순서
'''
1 = 1/1
2 = 1/2
3 = 2/1
4 = 3/1 
5 = 2/2
6 = 1/3
7 = 1/4
8 = 2/3
9 = 3/2
10 = 4/1
11 = 5/1
12 = 4/2
13 = 3/3
14 = 2/4
'''


N = int(input())
cnt = 1
chk = 0
while cnt < N:
    N -= cnt
    cnt += 1
    chk += 1
    
if chk % 2 != 0: # 짝수, 오름차
    # print(N,'/',chk+2-N)
    print(N, end='')
    print('/', end='')
    print(chk+2-N)
else:
    print(chk+2-N, end='')
    print('/', end='')
    print(N)