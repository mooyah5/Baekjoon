# N = int(input())
# arr = list(map(int, input().split()))
ints = [i for i in range(1,20)]
print(ints)
i = 0
while len(ints)>0:
    if ints[i]%2==0: 
        ints.remove(i)
        i += 1

    if ints[i]%3==0 :
        ints.remove(i)
        continue
    if ints[i]%5==0 :
        ints.remove(i)
        continue
    if ints[i]%7==0:
        ints.remove(i)
        continue
    if ints[i]%11==0:
        ints.remove(i)
        continue
    if ints[i]%13==0:
        ints.remove(i)
        continue
    if ints[i]%17==0:
        ints.remove(i)
        continue
    if ints[i]%19==0:
        ints.remove(i)
        continue

    # if ints[i]%2==0 or ints[i]%3==0 or ints[i]%5==0 or ints[i]%7==0 or ints[i]%11==0:
    #     ints.remove(ints[i])
print(ints)