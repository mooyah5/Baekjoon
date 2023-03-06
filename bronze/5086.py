# 배수와 약수
# Bronze 3

# 0 0 이 나올 때까지 두 수 A, B가 줄마다 공백을 구분하여 주어진다.
# A가 B의 약수면 factor, 배수면 multiple, 암것도아니면 neither을 출력한다.

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if B % A == 0:
        print('factor')
    elif A % B == 0:
        print('multiple')
    else:
        print('neither')
