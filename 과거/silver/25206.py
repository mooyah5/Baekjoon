# 너의 평점은
# Silver 5

# 졸업하려면 3.3이상이어야함. 전공평가 계산 ㄱㄱ

# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	  0.0
# P   계산에서 제외

# 입력
# 20줄에 걸쳐 수강과목명, 학점, 등급이 공백 구분

# 출력
# 전공평점 출력 (절대오차나 상대오차가 10^-4 이하이면 정답)


grade_table = {
    'A+': 4.5,
    'A0': 4.0,
    'B+':	3.5,
    'B0':	3.0,
    'C+':	2.5,
    'C0':	2.0,
    'D+':	1.5,
    'D0':	1.0,
    'F': 0.0,
    'P': -1,
}
sum_score = 0   # 총 학점
cnt = 0         # 나눠줄 학점 개수
for t in range(20):
    sub, score, grade = map(str, input().split())
    score = int(float(score))
    if grade == 'P':
        continue
    sum_score += grade_table[grade] * score
    cnt += score
print(round(sum_score / cnt, 6))
