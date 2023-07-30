# 명령 프롬프트
# Bronze 1

###############################################
# ## 230612 (1) 너무 길다

# import sys
# input = sys.stdin.readline

# # 입력 받아서 배열에 저장
# T = int(input())
# arr = [input().strip() for _ in range(T)]

# # 다른 단어 위치 찾기
# cnt = set()
# for i in range(1, T):
#     for j in range(len(arr[0])):
#         if arr[i - 1][j] != arr[i][j]:
#             cnt.add(j)

# # 출력
# answer = ""
# for i in range(len(arr[0])):
#     if i in cnt:
#         answer += "?"
#     else:
#         answer += arr[0][i]
# print(answer)


###############################################
# ## 230612 (2) 간결화
# (문자열을 문자리스트로 빼서 replace 대신 직접 바꾸는 방법으로 출력 줄이기)
import sys
input = sys.stdin.readline

T = int(input())
arr = [list(input().strip()) for _ in range(T)]
ans = arr[0]

cnt = set()
for i in range(1, T):
    for j in range(len(arr[0])):
        if arr[i - 1][j] != arr[i][j]:
            ans[j] = "?"

print("".join(ans))

