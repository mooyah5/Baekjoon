# bronze 2 대표값
# 한 줄에 하나씩 자연수가 주어진다(1000보다 작은 10의 배수)
# 첫째 줄에 평균을, 둘째 줄에 최빈값을 출력

arr = [int(input()) for i in range(10)]

# 평균 = 합계 // 개수
print(sum(arr) // 10)

# 최빈값 => counting sort 사용해 보기
counts = [0 for i in range(1000)]
for n in arr:
    counts[n] += 1
print(counts.index(max(counts)))

