T = int(input())
for _ in range(T):
    F = int(input())    # 층 수 0~F층
    N = int(input())    # 방 개수 1~N개

    # 1. 0~F층, N번방이 있는 아파트를 생성한다. (0으로 채움)
    arr = [[0 for i in range(N)] for i in range(F+1)]

    # 2. 0층에 1~N까지 방 번호를 채워준다.
    arr[0] = [i for i in range(1, N+1)]

    # 3. 각 방에 아래층 1~N번 번호를 합쳐서 채워준다.
    for f in range(1, F+1):
        i = 1
        for n in range(N):
            arr[f][n] = arr[f-1][n] + arr[f][n-1]   # 아래층 전 번호 + 현재층 이전번호까지

    print(arr[F][N-1])
