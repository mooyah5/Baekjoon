# 좌표 압축
# Silver 2

# 수직선 위 N개의 좌표가 있는데 압축하려고 한다.
# 좌표 압축: 해당 좌표 값을 그 값보다 작은 좌표값들의 개수로 대체함
# 오름차 정렬해서 중복제거하면 그 인덱스가 대체할 좌표값의 개수가 됨

n = int(input())
arr = list(map(int, input().split()))
# 좌표압축하기 위해 오름차정렬 및 중복 제거
arr_set_sorted = sorted(set(arr))

# 딕셔너리로 좌표압축 찾는 시간 절약 (.index() 대신)
new = {}
for i in range(len(arr_set_sorted)):
    new[i] = arr_set_sorted[i]
convert_new = {v: k for k, v in new.items()}

ans = []
for a in arr:
    ans.append(convert_new[a])
print(*ans)


# # 딕셔너리에서 value를 이용해 key를 찾는 방법
# [k for k, v in list.items() if v == '찾을key']
# # 자주 value를 이용해 key를 찾을 거라면, 뒤집어 저장해 놓는다.
# convert_new = {v: k for k, v in new.items()}
