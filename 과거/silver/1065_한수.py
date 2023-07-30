N = int(input())

# 두자리수면 그 자체가 답
if N <= 99:
    res = N
# 세자리수면 99 + cnt
elif 99 < N < 1000: # 세자리수면
    cnt = 0
    for i in range(100, N+1):
        nums = []
        for j in str(i):
            nums.append(int(j))
        if nums[1] - nums[0] == nums[2] - nums[1]:
            cnt += 1
    res = cnt + 99
# 네 자리 수면 하드콛잉
elif N == 1000:
    res = 144
print(res)