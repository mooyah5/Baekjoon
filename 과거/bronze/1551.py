#1 

n, k = map(int, input().split())
list_ = list(map(int, input().split(',')))
list_2 = []
for _ in range(k):
    for i in range(len(list_)-1):
        list_2.append(list_[i+1]-list_[i])
    list_ = list_2
    list_2 = []
print(*list_, sep=',')

#2 리스트 컴프리헨션

# n, k = map(int, input().split())
# list_ = list(map(int, input().split(',')))
# list_2 = []
# for _ in range(k):
#     list_2 = [list_[i+1]-list_[i] for i in range(len(list_)-1)]
#     list_ = list_2
# print(*list_, sep=',')
