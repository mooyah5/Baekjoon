a = int(input())
b = input()
c = []
for i in b:
    c.append(a*int(i))
c.reverse()
    
for i in c:
    print(i)
print(a*int(b))