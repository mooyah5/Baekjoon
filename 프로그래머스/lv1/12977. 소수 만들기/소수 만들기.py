# ans = []

def solution(nums):
    
#     # Make : 길이가 3인 부분수열을 구하는 함수
#     def Make(i, arr):
#         global ans

#         if len(arr) >= 3:
#             ans.append(arr[:])
#             return

#         if i >= len(nums):
#             return

#         arr.append(nums[i])
#         Make(i + 1, arr[:])
#         arr.pop()
#         Make(i + 1, arr[:])
#         return ans
#     ans = Make(0, [])
    from itertools import combinations as cb
    ans = cb(nums, 3)
    
    # 소수가 몇 개인지 구하기
    cnt = 0
    for a in ans:
        state = True
        N = sum(a)
        for i in range(2, N):   # 2부터 N-1까지의 수 중 N을 나누었을 때 나누어 떨어지면 소수가 아님.
            if N % i == 0:
                state = False
                break
        if state:
            cnt += 1
    return cnt