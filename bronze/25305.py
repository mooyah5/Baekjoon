# 커트라인
# Bronze 2

# 상 받는 사람 중 가장 낮은 점수를 출력

N, k = map(int, input().split())      # 응시자 수, 상받는학생 수
arr = list(map(int, input().split()))  # 각 응시자 점수
print(sorted(arr, reverse=True)[k-1])
