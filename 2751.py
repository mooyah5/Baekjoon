# 병합정렬

# 1. 데이터를 절반씩 나누어 끝까지 갔다가 (분할)
# 2. 다시 절반식 합치면서 그 안에서 정렬 (정복)

## 병합정렬 재귀
def merge_sort(array):
    mid = len(list_str)//2 # 리스트 길이 절반
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0

    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            

t = int(input())
list_str = []
for _ in range(t):
    list_str.append(int(input()))

print(merge_sort(list_str))