# list = []
# for i in range(9):
#     list.append(int(input()))

# a = 0

# for j in list:
#     if list[j+1] > list[j]:
#         a = list[j+1]

# print(max(list))
# print()

numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

cnt = 0 # 개수
for i in numbers:
	cnt += 1
	
for i in range(cnt):
	for j in range(cnt-i-1):
        if numbers[j] > numbers[j+1]:
		numbers[j+1], numbers[j] = numbers[j], numbers[j+1]

a = cnt//2
print(number[a])