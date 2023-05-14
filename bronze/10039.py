# 평균 점수
# B4

scores = []
for i in range(5):
    scores.append(int(input()))

# print(scores)
for i in range(5):
    if scores[i] <= 40:
        scores[i] = 40
print(sum(scores) // 5)
