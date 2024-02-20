n = int(input())
a = []
ans = 0
def func(arr):
  global ans
  if len(arr) > n:
    return
  for i in range(3):
    arr.append(i)
    func(arr)
    arr.pop()
  if len(arr) == n:
    num = int(''.join(map(str, arr)))
    if num != 0 and num % 3 == 0 and len(str(num)) == n:
      ans += 1


func(a)
print(ans)