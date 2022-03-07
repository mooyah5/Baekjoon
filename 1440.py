list_ = list(map(int, input().split(':'))) 
sum = 0
for i in range(3):
  for j in range(3):
    for k in range(3):
      # list[?] 에서 인덱스가 겹치지 않게 (0, 1, 2)(0, 2, 1)... 이런식
      if i != j and j != k and k != i: 
        # 시, 분, 초의 경우에 속하면 sum +=1
        if 1 <= list_[i] <= 12 and 0<=list_[j]<=59 and 0<=list_[k]<=59:
          sum += 1
print(sum)