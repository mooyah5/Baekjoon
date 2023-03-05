# 스택 수열
# Silver 2

T = int(input())
lst = []
for tc in range(T):
    n = int(input())
    lst.append(n)
stack = []

i = 1
while i <= T:
    print(i, stack, lst)
    if i == lst[-1]:
        lst.pop(0)
        stack.pop(-1)
        print('-')
    stack.append(i)
    print('+')

    i += 1
