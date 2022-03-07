# 1. 0이 나올때까지 입력받아 리스트에 넣고 0은 삭제
data = []
while '0' not in data:
    data.append(input())
data.remove('0')

# 2. str로 인식함. 거꾸로한 값이 원본가 동일하면 yes 출력
for d in range(len(data)):
    reverse_d = ''
    for i in range(len(data[d])-1, -1, -1):
        reverse_d += data[d][i]
    if reverse_d == data[d]:
        print('yes')
    else:
        print('no')