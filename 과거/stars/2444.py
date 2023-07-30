n = int(input())
for i in range(n):
    print((n-1-i) * ' ' + (1+(2*i)) * '*')
    
for i in range(n-2,-1,-1):  # 3,2,1,0
    print((n-i-1)*' ' + ((i*2)+1)*'*')
