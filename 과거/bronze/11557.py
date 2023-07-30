# Bronze 1
# 올해의 양조장

# 학교별 한 해 술 소비량이 주어진다.
# 가장 술 소비가 많은 학교는?

T = int(input())        # 테스트케이스 개수
for tc in range(T):
    dic = dict()
    N = int(input())    # 학교 개수
    for i in range(N):
        U, cons = map(str, input().split())
        cons = int(cons)
        dic[U] = cons   # 딕셔너리에 key(학교), value(소비량) 저장
    max_U = max(dic, key=dic.get)   # value 값이 높은 학교 출력
    print(max_U)

# max에는 선택 사용 가능한 인자로 key와 default가 있다.
# key: 무엇을 기준으로 max값을 구할 것인지
# max 함수의 두번째 인자로 key = len을 주면 길이 기준으로 구함.
# default: 빈 배열에서 max 구하면 ValueError 발생하므로, 비어있을 경우를 대비한 값을 지정
