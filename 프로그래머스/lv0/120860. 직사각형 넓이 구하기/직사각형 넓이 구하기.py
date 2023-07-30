def solution(dots):
    lst1 = []
    lst2 = []
    for i in range(4):
        lst1.append(dots[i][0])
        lst2.append(dots[i][1])
    return (max(lst1)-min(lst1)) * (max(lst2) - min(lst2))