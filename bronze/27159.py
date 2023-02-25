# Bronze 3
# 노 땡스!

# 3~35 카드중 카드 N개를 받는다.
# 1씩만 차이나는 카드끼리 묶어서
# 그룹별로 가장 작은 수끼리 합하여 출력

N = int(input())    # 카드의 개수
arr = list(map(int, input().split(' ')))
arr2 = []
pre = [arr[0]]
ans = arr[0]
for i in range(1, N):
    if pre[-1] + 1 == arr[i]:
        pre.append(arr[i])
        # print('이어짐', arr[i], pre)
    else:
        pre.append(arr[i])
        ans += arr[i]
# print(pre)
print('ans', ans)
