import sys
id_list = list(map(int, sys.stdin.readline().split()))
squared_nums = []
for i in id_list:
    squared_nums.append(i**2)
print(sum(squared_nums)%10)
