# 중간계 전쟁
# B3

# 중간계 전쟁 군대 참여자 각 종족의 점수
Gandalf = [1, 2, 3, 3, 4, 10]
Sauron = [1, 2, 2, 2, 3, 5, 10]

# 첫째줄에 전투 개수 N
N = int(input())

# 각 전투마다 두줄 씩 차지 (한줄씩 간달프, 사우론 종족원 수가 주어짐)
# 각 전투에 대해서, "Battle"과 전투 번호를 출력한다.
# 간달프의 군대가 이긴다면 "Good triumphs over Evil"
# 사우론의 군대가 이긴다면 "Evil eradicates all trace of Good"
# 점수의 합이 같아 이기는 쪽이 없다면 "No victor on this battle field"

for battle in range(1, N+1):
    ganScore = sauScore = 0
    gan = list(map(int, input().split()))
    sau = list(map(int, input().split()))
    for i in range(6):
        ganScore += gan[i] * Gandalf[i]
    for i in range(7):
        sauScore += sau[i] * Sauron[i]
    print('Battle ' + str(battle) + ': ', end='')
    if ganScore > sauScore:
        print('Good triumphs over Evil')
    elif ganScore < sauScore:
        print('Evil eradicates all trace of Good')
    else:
        print('No victor on this battle field')
