# 크로아티아 알파벳
# 실버5

words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()

for word in words:
    S = S.replace(word, '*')
print(len(S))