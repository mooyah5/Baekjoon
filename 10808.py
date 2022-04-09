# 알파벳 개수 B2

# 소문자로만 이루어진 단어 S에
# 각 알파벳이 몇 개가 있는지 출력
# print(ord('a')) = 97

S = input()
arr = [0 for i in range(26)]
for i in range(len(S)):
    arr[ord(S[i])-97] += 1
print(*arr)
    