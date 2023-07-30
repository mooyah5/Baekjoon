# 중복 빼고 정렬하기

# 첫째줄 1 <= n <= 100,000
# n개의 정수 (절댓값이 1000이하)가 공백을 두고 입력

# 출력 오름차순 정렬 결과 (같은 수는 한 번만)

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))
print(*arr)