# def d(n):
#     total = n
#     for i in str(n):
#         total += int(i)
#     if total <= 10000:
#         print(total)
#         return d(total)

# d(33)


# def d(n):
#     pass

# d()

# 셀프넘버

# def fff(x):
#     a = str(x)
#     b = x
#     for i in a:
#         b += int(i)
#     return b
# listtt = list(range(1, 10001))
# for i in range(1, 1001):
#         if fff(i) == j:
#             listtt.remove(i)
# print(listtt)

# nums = set(range(1, 10001))
# set_a = set()
# c = set()

# for i in range(1, 10001): #39
#     c = 0
#     c += i
#     for j in str(i): # 3, 9
#         c += int(j)
#     set_a.add(c)

# self_num = sorted(nums - set_a)
# for i in self_num:
#     print(i)


###
# 소수판별 에라토스테네스 체 

lst = set([i for i in range(1,10001)])
notSelf = set()
sum = 0

for i in lst:
    for j in str(i):
        sum += int(j)
    if sum+i in lst:
        notSelf.add(sum+i)
    sum = 0

for k in sorted(lst - notSelf):
    print(k)        
