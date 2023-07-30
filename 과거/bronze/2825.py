# 대회 or 인턴

# 여2, 남1으로 팀을 결성하는 게 원칙
# N명의 여학생, M명의 남학생이 있고, 그중 K명은 반드시 참여해야 한다.
# 만들 수 있는 최대의 팀 수는?

N, M, K = map(int, input().split())
cnt = 0

while True:
    # 여 혹은 남학생 수가 팀 결성하긴 부족하거나, K명을 따로 뺄 수 없을 때 출력
    if N < 2 or M < 1 or N+M-3 < K:
        print(cnt)
        break
    # 팀 결성에 충분한 여, 남학생 수가 있으면서, 팀을 결성한 후에도 남은 학생 수가 K보다 크면
    if N > 1 and M > 0 and N+M-3 >= K:
        N -= 2
        M -= 1
        cnt += 1
