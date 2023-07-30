# 요세푸스 문제 0
# Silver 5

# 원을 둘러 앉은 1~N번 사람들
# 순서대로 K번째 사람을 제거한다.
# N = 7, K = 3 이라면, 제거 순서는 [3, 6, 2, 7, 5, 1, 4]

N, K = map(int, input().split())
arr = [1 for _ in range(N + 1)]
res = []

i = -1  # 첫번째 제거는 한 칸 모자라므로 -1에서 시작
for q in range(N - 1):  #  N-1번 반복
    count = 0  # 몇번 이동했는지 나타낼 변수

    while count < K:  # K번 이동하면 종료
        i = (i + 1) % N  # i인덱스가 순환하므로 나머지연산 활용
        if arr[i]:  # 제거대상이면
            count += 1  # 카운트 증가

    arr[i] = 0  # K번 이동 후 카운트 증가했으므로 제거처리
    res.append(i + 1)  # 현재 제거된 사람의 번호 출력
res.append(arr.index(1) + 1)  # 미처 제거못한 마지막 사람 번호 출력

print("<", end="")
print(", ".join(map(str, res)), end=">")
