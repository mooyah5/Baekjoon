# 나이순 정렬
# 첫째줄 n
# n줄에 나이와 이름이 가입순서대로 주어진다.
# 나이 증가 순으로, 먼저 가입한 순으로 정렬

n = int(input())
arr = []
for i in range(n):
    age, name = map(str,input().split())
    age = int(age)
    arr.append([age, name])
    
arr.sort(key=lambda x: x[0])

for a in arr:
    print(*a)