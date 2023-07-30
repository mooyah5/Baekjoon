def boy(num):
    i = 1  # 배수에 더할 수
    while num * i <= len_switches:
        idx = num * i - 1
        switches[idx] = 1 - switches[idx]  # 0 <-> 1 반전
        i += 1


def girl(num):
    num -= 1  # 인덱스이므로 번호 - 1
    switches[num] = 1 - switches[num]
    s, e = num, num  # 대칭이면 반전시킬 범위를 구하기 위해 start, end 포지션을 num 인덱스로부터 시작
    while s >= 0 and e < len_switches:
        if switches[s] == switches[e]:
            switches[s] = 1 - switches[s]
            switches[e] = 1 - switches[e]
            s -= 1
            e += 1
        else:
            break

len_switches = int(input())
switches = list(map(int, input().split()))
len_students = int(input())

for _ in range(len_students):
    sex, num = map(int, input().split())
    if sex == 1:  # 남학생
        boy(num)
    else:  # 여학생
        girl(num)

# 출력 조건: 한 줄에 20개씩 출력한다.
for i in range(len_switches):
    if (i + 1) % 20 == 0:  # 참고: % 연산자가 +보다 우선순위가 높다.
        print(switches[i], end="\n")
    else:
        print(switches[i], end=" ")
