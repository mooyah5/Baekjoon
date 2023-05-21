# 애너그램
# B1

# 두 단어 A, B가 애너그램인지 아닌지 구하기

# ord('a') = 97
# chr(122) = 'z'

# 230522
n = int(input())
for _ in range(n):
    dict_ = {}
    for i in range(97, 123):
        dict_[chr(i)] = 0

    A, B = map(str, input().split())
    for a in A:
        dict_[a] += 1
    for b in B:
        dict_[b] -= 1

    for k, v in dict_.items():
        if v != 0:
            print(A, "&", B, "are NOT anagrams.")
            break
    else:
        print(A, "&", B, "are anagrams.")
