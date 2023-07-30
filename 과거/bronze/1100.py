list_ = []
for i in range(8):
    list_.extend(list(input().split())) #extend()로 문자열 개별로 이차원 리스트 생성

white_ = 0  #흰 면에 말이 있으면 cnt+1

# 0, 2, 4, 6번째 줄의 0, 2, 4, 6번째 칸에 흰 말 있냐
for i in range(0, 8, 2):
    for j in range(0, 8, 2): 
        if list_[i][j] == 'F':
            white_ += 1

# 1, 3, 5, 7 번째 줄의 1, 3, 5, 7번째 칸에 흰 말 있냐
for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        if list_[i][j] == "F":
            white_ += 1
            
print(white_)