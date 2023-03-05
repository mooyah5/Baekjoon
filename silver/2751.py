# 병합정렬

# 1. 데이터를 절반씩 나누어 끝까지 갔다가 (분할)
# 2. 다시 절반식 합치면서 그 안에서 정렬 (정복)

## 병합정렬 재귀
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1

    return array
            
n = int(input())
arr = [int(input()) for _ in range(n)]
res = merge_sort(arr)
print('\n'.join(str(n) for n in res))

### 파이썬 내장함수
# n = int(input())
# nums = list(int(input()) for _ in range(n))
# nums.sort()
# for n in nums:
#     print(n)
# # print('\n'.join(str(i) for i in nums))