while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b ==0 and c==0:       # 중단조건
        break
    
    arr = [a, b, c]
    arr.sort()
    
    if arr[0]**2 + arr[1]**2 == arr[2]**2:           # 직각삼각형비
        print('right')
    else:
        print('wrong')