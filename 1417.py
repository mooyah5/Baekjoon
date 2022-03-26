n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dasom = arr[0]
people = arr[1::]
cnt = 0
people.sort()
if n == 1:
    print(0)
else:
    while dasom <= max(people):
        people[-1] -= 1
        dasom += 1
        cnt += 1
        people.sort()
    # ta_sum = 0
    # for i in range(1, n):
    #     ta_sum += arr[i]
    # if arr[0] > ta_sum/(n-1):
    #     break
    print(cnt)
