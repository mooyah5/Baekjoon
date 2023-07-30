# 입력받기
N, k = map(int, input().split())
list_ = []
for _ in range(N):
    list_.append(list(map(int, input().split())))

# 여0/남1 으로 구분
w0 = []
m1 = []
for i in range(N):
    if list_[i][0] == 0:
        w0.append(list_[i][1])
    else:
        m1.append(list_[i][1])
w0.sort()
m1.sort()

# # 3명 이상이면 분리 count() 사용
cnt = 0
for i in range(1, 7):
    if m1.count(i) > k:
        for _ in range(k):
            m1.remove(i)
        cnt += 1
    continue
m1 = list(set(m1))
cnt += len(m1)

for i in range(1, 7):
    if w0.count(i) > k:
        for _ in range(k):
            w0.remove(i)
        cnt += 1
    continue
w0 = list(set(w0))
cnt += len(w0)

print(cnt)


###
#1학년 남학생 (1, 1)
# N, K = map(int, input().split())
# list_ = []
# for _ in range(N):
#     list_.append(list(map(int, input().split())))

# boy_1 = []
# for li in list_ :
#     if li[0] == 1 and li[1] == 1:
#         boy_1.append(li)
# print(boy_1)

# if len(boy_1) % 2 == 0:
#     print(round(len(boy_1)/2))
# else:
#     print(round(len(boy_1/2 +1)))