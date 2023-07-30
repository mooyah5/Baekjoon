# 과제 안 내신 분..?
# 1~30까지의 번호가 한줄에 하나씩 28줄 들어온다
# 들어오지 않은 번호는?

arr = [0 for i in range(30)]
for i in range(28):
    n = int(input())
    arr[n-1] = 1
first = arr.index(0)
print(first+1)
second = arr.index(0, first+1, 30)
print(second+1)
