T = int(input())
for i in range(T):
    rep, strings = map(str, input().split())
    txt = ''
    for j in strings:
        txt += j*int(rep)
    print(txt)
    P = int(rep) * strings
    print(P)

# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i
#     print(text)