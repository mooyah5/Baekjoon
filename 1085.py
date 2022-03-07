x, y, w, h = map(int, input().split())

distance = [h-y, y, w-x, x]
print(min(distance))