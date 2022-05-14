a = int(input())

# a = [0 for i in range(new_avg)]   
b = list(map(int, input().split()))

max_score = max(b)
c = [0 for i in range(a)]
total = 0
for i in range(a):
    c[i] = b[i] / max_score * 100
    total += c[i]
    
avgg = total / a
print(avgg)