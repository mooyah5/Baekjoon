a = input()
b = input()
c = input()

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = [i for i in range(10)]
times = [10**i for i in range(10)]

aa = value[color.index(a)]
bb = value[color.index(b)]
cc = times[color.index(c)]

print((aa*10+bb)*cc)