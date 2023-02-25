# Bronze 1
# 약수들의 합

# n이 자신을 제외한 모든 약수들의 합과 같으면 완전수
# 예) 6은 1+2+3=6 으로 완전수이다.
# n이 완전수이면 6 = 1 + 2 + 3 이런 식으로 출력하고,
# 그렇지 않으면 n is NOT perfect. 를 출력한다.
# 한줄에 하나씩 n이 입력되며, 테케가 없으면 막줄에 -1가 입력됨

state = True
while (state):
    n = int(input())
    measure = []
    if n == -1:
        state = False
        continue

    for i in range(1, n):
        if n % i == 0:
            measure.append(i)

    if sum(measure) == n:
        print(n, '= ', end='')
        print(*measure, sep=' + ')
    else:
        print(n, 'is NOT perfect.')
