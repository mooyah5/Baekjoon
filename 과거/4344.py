
cases = int(input())
a = [0 for i in range(cases)]
for i in range(cases):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    count = 0
    
    for score in nums[1:]:
        if score > avg:
            count += 1
    perc = count / nums[0] * 100
    print(f'{perc:.3f}%')
