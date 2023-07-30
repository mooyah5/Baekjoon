# 가장 긴 단어 S4

# 알파벳과 하이픈으로만 이루어진 단어
# 단어와 다른문자로 이루어진 글이 주어졌을 때, 가장 긴 단어는?

#### 1

# max_len = 0
# max_s = ''
# a = 1
# while a==1:
#     try:
#         S = input().split()
#         for s in S:
#             cnt = 0
#             for i in range(len(s)):
#                 if s[i:] == 'E-N-D':
#                     # print(max_len)
#                     print(max_s.lower())
#                     a = 0
#                     break
#                 if s[i].isalpha() or s[i] == '-':
#                     cnt += 1
#             if cnt > max_len:
#                 max_len = cnt
#                 max_s = s
#     except EOFError:
#         break




#### 2

data = []
while True:
    data.extend(input().split())
    if data[-1] == 'E-N-D':
        break

arr = []
for d in data:
    tmp = ''
    for i in range(len(d)):
        if d[i] == '-' or d[i].isalpha():
            tmp += d[i].lower()
    arr.append(tmp)

max_len = 0
max_s = ''
for a in arr:
    if len(a) > max_len:
        max_len = len(a)
        max_s = a
print(max_s)