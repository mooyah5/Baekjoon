# 별 찍기 -6 B3
# 5
'''
*********
 *******
  *****
   ***
    *
'''

n = int(input())
for i in range(n,-1, -1):
    print(' '*(n-i)+(i*2-1)*'*')