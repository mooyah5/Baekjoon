T = int(input())
list_str = []
for i in range(T):
    list_str.append(input())
list_str = list(set(list_str)) # 중복 제거

list_str.sort() # 문자로 정렬
list_str.sort(key = len) # 문자열 길이로 정렬

# for i in range(1, len(list_str)):
#     for j in range(0, len(list_str)-1):
#         if len(list_str[j]) > len(list_str[j+1]):
#             list_str[j+1], list_str[j] = list_str[j], list_str[j+1]
#         elif len(list_str[j]) == len(list_str[j+1]):
#             for k in range(1, len(list_str[j])) :
#                 for l in range(0, len(list_str[j])-1):
#                     if ord(list_str[j][l]) > ord(list_str[j+1][l]):
#                         list_str[j+1], list_str[j] = list_str[j], list_str[j+1]
# print(list_str)


for i in list_str:
    print(i)