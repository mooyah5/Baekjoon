import fractions
def solution(numer1, denom1, numer2, denom2):
    answer = []
    # 1. 분수 합 더하기 (분자/분모 따로 구함)
    numer3 = numer1*denom2 + denom1*numer2
    denom3 = denom1 * denom2
    
    # 예외) 만약 분수의 합이 1이면 따로 출력해준다.
    if numer3 == denom3:
        return [1, 1]
    
    # 2. 기약분수 만들기 (분자, 분모를 각각 최대공약수로 나눠주기)
    biggerNum = max(numer3, denom3)     # 분자와 분모 중에 더 큰 값 (최대공약수 구하기 위함)
    gcd = -1    # 최대공약수
    for i in range(1, biggerNum):
        if numer3 % i == 0 and denom3 % i == 0:
            gcd = i

    return numer3/gcd, denom3/gcd