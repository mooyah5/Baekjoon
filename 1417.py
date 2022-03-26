n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dasom = arr[0]          # 다솜 표
people = arr[1::]       # 다른 후보들 표
cnt = 0                 # 최소 빼올 득표수
people.sort()           # 후보들 표 정렬
if n == 1:              # 후보가 다솜이 혼자면 0 출력
    print(0)
else:
    while dasom <= max(people): # 다솜표가 최대 타인표를 넘어서면 반복 멈춰
        people[-1] -= 1     # 가장 많은 득표수의 표를 하나 빼서
        dasom += 1          # 다솜이 주고
        cnt += 1            # cnt +1
        people.sort()       # 후보들 표 재정렬
    print(cnt)
