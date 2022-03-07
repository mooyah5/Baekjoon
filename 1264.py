mo = 'aeiouAEIOU' # 모음 모음집!
list_ = []
while True:
    list_.append(input())   # 리스트에 한줄씩 입력받음
    if list_[-1] == '#': # 마지막 입력값이 #이면 입력 멈춰!
        break
list_.remove(list_[-1]) # 마지막 입력받은 '#' 삭제

for i in list_:
    sum = 0
    for j in i:
        if j in mo: # 각각의 문자가 모음에 속하면 sum +1
            sum += 1
    print(sum)
