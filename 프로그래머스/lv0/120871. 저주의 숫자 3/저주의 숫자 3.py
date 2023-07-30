def solution(n):
    answer = 0
    i = 0
    num = 0
    while True:
        if i == n: break
        tmpNum = num + 1
        if '3' in str(tmpNum) or tmpNum % 3 == 0:
            num += 1
        else:
            num += 1
            i += 1
    return num