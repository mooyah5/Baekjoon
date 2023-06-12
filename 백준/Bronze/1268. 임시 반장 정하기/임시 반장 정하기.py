# 임시 반장 정하기
# Bronze 1

# 230613
import sys

input = sys.stdin.readline
n = int(input())  # 학생 수
arr = [list(map(int, input().split())) for _ in range(n)]  # 학생 리스트 받아

# 학생 당 반 겹친 개수 세어줄 딕셔너리
students = dict()
for i in range(1, n + 1):
    students[i] = 0

for i in range(n):  # 학생 한명씩
    for j in range(n):  # 다른 학생과 비교
        tmp = False  # 이미 해당 학생과 같은 반이었는지 체크
        for k in range(5):  # 학년별로
            # 나 자신이 아니고, 반 번호가 같으면 개수 +1 (이미 같은반이면 break)
            if not tmp:
                if i != j and arr[i][k] == arr[j][k]:
                    students[i + 1] += 1
                    tmp = True
            else:
                break

# 최대 value 가진 key(학생번호) 찾기
print(max(students, key=students.get))
