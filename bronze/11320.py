# Bronze 3
# 삼각무늬 - 1

# 삼각셩 A인 정삼각형을 그보다 작거나 같은 B가 완전히 덮으려면 몇 개 필요한지

T = int(input())    # 테스트 개수
for t in range(T):
    A, B = map(int, input().split(' '))
    x = A // B      # 변 길이를 나눈 값만큼 곱할 값을 지정
    if A % B:       # 나머지가 존재하면 곱할 값을 1 추가
        x += 1
    print(x**2)     # 필요 개수는 1, 4, 9, 16의 규칙으로 증가
