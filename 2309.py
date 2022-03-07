# list_ = []
# for _ in range(9):
#     list_.append(int(input()))

# chas = sum(list_)-100

# for i in range(0, 8):
#     for j in range(i+1, 9):
#         if list_[i] + list_[j] == chas:
#             list_.remove(list_[j])
#             list_.remove(list_[i])
#             break
#     if len(list_) == 7:
#         break

# list_.sort()
# for i in list_:
#     print(i)

### 투포인터 도전
list_ = []
for _ in range(9):
    list_.append(int(input()))
list_.sort()

cha = sum(list_) - 100
l = 0
r = 8

while l < r :
    if list_[l] + list_[r] == cha:
        list_.remove(list_[r])
        list_.remove(list_[l])
        break
    elif list_[l] + list_[r] < cha:
        l += 1
    else: # 두 포인터의 합이 cha보다 크면
        r -= 1
    if l > len(list_) or r < 0:
        break

print(list_)


