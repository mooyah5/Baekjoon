# Bronze 1
# Yangjojang of The Year

# 학교별 한 해 술 소비량이 주어진다.
# 가장 술 소비가 많은 학교는?

T = int(input())        # 테스트케이스 개수
for tc in range(T):
    dic = dict()
    N = int(input())    # 학교 개수
    for i in range(N):
        U, cons = map(str, input().split())
        cons = int(cons)
        dic[U] = cons
    # print(dic)
    max_U = max(dic, key=dic.get)
    print(max_U)
