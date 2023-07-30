# 통계학
# Silver 3

# 입력
# 줄의 개수 N (홀수)
# N개의 줄마다 정수 (<=4000)가 주어진다.

# 출력
# 1. 산술평균 = N개의 수들의 합을 N으로 나눈 값 (소수점이하 첫째 자리에서 반올림)
# 2. 중앙값 = 오름차순으로 나열하고 중앙에 위치한 값
# 3. 최빈값 (여러 개면 두 번째로 작은 값)
# 4. 범위 = 최댓값과 최솟값의 차이

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()                  # 중앙값 구하기 위해 정렬


# 1. 산술평균
print(round(sum(arr)/N))


# 2. 중앙값
print(arr[N//2])


# 3. 최빈값
# newArr라는 카운팅 배열 선언 및 초기화
# newArr[0]에는 최솟값부터 최댓값까지의 인덱스를 넣어 놓는다.
# newArr[1]에는 인덱스에 해당하는 숫자의 빈도수(개수)를 넣기 위해 0으로 초기화
newArr = [[i for i in range(min(arr), max(arr)+1)],
          [0 for _ in range(min(arr), max(arr)+1)]]

# 빈도수 조사하여 newArr[1]에 1씩 추가
for a in arr:
    newArr[1][newArr[0].index(a)] += 1

# 최빈값을 리스트에 담기 위해
# 리스트에 든 원소들을 함수에 적용시켜 결과가 최빈값들의 인덱스로 새 리스트 생성
modes = list(filter(lambda x: newArr[1][x] == max(
    newArr[1]), range(len(newArr[0]))))

# 여러 개면 그 중 두 번째로 작은 수를 출력
if len(modes) > 1:
    print(newArr[0][modes[1]])
else:
    print(newArr[0][modes[0]])


# 4. 범위
print(max(arr)-min(arr))
