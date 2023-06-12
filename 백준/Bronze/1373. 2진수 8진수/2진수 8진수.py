# 2진수 8진수
# 230613
# 2진수 주어졌을 때 8진수 변환하기
n = input()

# # 2진수를 10진수로 (1- 시간초과)
# dec = 0
# j = 1  # 1, 2, 4, 8, ... 곱해줄 숫자
# for i in range(len(n) - 1, -1, -1):  # 이진수 뒷 숫자부터
#     dec += int(str(n)[i]) * j
#     j *= 2

# 2진수를 10진수로 (2)
dec = int(n, 2)

# 10진수를 8진수로
ans = oct(dec)
print(ans[2:])
