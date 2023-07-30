import sys
n = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
s = 0
e = 0
max_leng = 0

while s <= e and e < len(S):
    if max_leng < len(S[s:e+1]):
        max_leng = len(S[s:e+1])

    if len(set(S[s:e+1])) <= n:
        e += 1

    if len(set(S[s:e+1])) > n:
        s += 1
    
print(max_leng)

# a = 'abbcaccba'
# print(a[1:3+1]) #bbc