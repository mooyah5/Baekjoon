# 230613
import sys

input = sys.stdin.readline
n = int(input())  # 학생 수
arr = [list(map(int, input().split())) for _ in range(n)]

dict_ = dict()
for i in range(1, n + 1):
    dict_[i] = 0

for i in range(n):  # 학생 한명씩
    for j in range(n):  # 다른 학생과 비교
        tmp = False  # 이미 해당 학생과 같은 반이었는지 체크
        for k in range(5):  # 학년별로
            # 스스로 점검하지 않고, 나와 다른 학생의 번호가 같으면
            if not tmp:
                if i != j and arr[i][k] == arr[j][k]:
                    dict_[i + 1] += 1
                    tmp = True
            else:
                break

max_num = -100
max_man = 1
for k, v in dict_.items():
    if v > max_num:
        max_num = v
        max_man = k
print(max_man)
