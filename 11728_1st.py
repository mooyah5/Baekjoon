# len_a, len_b = map(int,input().split())
list_a = []
list_b = []
list_a.extend(map(int, input().split()))
list_b.extend(map(int, input().split()))
list_ = list_a +list_b
list_.sort()
for i in list_:
    print(i, end=' ')
