n = int(input())
for i in range(n-1,-1,-1):  # 3,2,1,0
    print((n-i) * '*' + ((i*2))*' ' + (n-i) * '*')
for i in range(n-1):
    print((n-i-1) * '*' + ((2*(i+1))) * ' ' + (n-i-1) * '*')
    

