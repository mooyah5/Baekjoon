# 시리얼 번호 S3
# 모든 시리얼 번호는 알파벳 대문자와 숫자로 이루어짐

# 시리얼 순서는
# 1. 길이가 짧은 것이 먼저
# 2. 길이가 같다면, 자리수 합이 작은 게 먼저(숫자만 더함)
# 3. 1과2로 안 되면, 사전순으로 비교(숫자<알파벳)

# n = int(input())
# arr = [input() for i in range(n)]

# arr.sort(key=lambda x: (len(x), sum(x), ord(x)))

# for a in arr:
#     print(a)