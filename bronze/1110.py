N = input()
result = 100

if int(N) < 10 :
    ar = '0' + N[0]
else :
    ar = N[0] + N[1]

count = 0
while int(N) != int(result) :

    a = int(ar[0])
    b = int(ar[1])
    if ((a + b) < 10) :
        sum = '0' + str(a+b)
    else :
        sum = str(a+b)

    ar = str(b) + sum[1]
    result = str(b) + sum[1] #result 왜 넣는지 아직 이해 못함

    count += 1

print (count)

