# 16진수 -> 10진수

in16 = input('16진수를 입력하세요.')

inlist = list(in16)
inlen = len(inlist)

dec = 0
n = 1
for i in inlist :
    if i in ('abcdef'):
        if i == 'A' or 'a':
            i = '10'
        if i == 'b':
            i = '11'
        if i == 'c':
            i = '12'
        if i == 'd':
            i = '13'
        if i == 'e':
            i = '14'
        if i == 'f':
            i = '15'
    
    dec += int(i)*(16**(inlen-n))
    n += 1
print(dec)

#A 넣으면 이상함