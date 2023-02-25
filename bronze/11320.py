# Bronze 3
# 삼각형 - 1

# 삼각셩 A인 정삼각형을 그보다 작거나 같은 B가 완전히 덮으려면 몇 개 필요한지

T = int(input())    # 테스트 개수
for t in range(T):
    A, B = map(int, input().split(' '))
    x = A // B
    if A % B:
        x += 1
    print(x**2)
