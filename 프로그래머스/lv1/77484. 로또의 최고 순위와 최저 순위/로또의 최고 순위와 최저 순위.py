def solution(lottos, win_nums):
    
    def rank(score):    # 점수를 순위로 반환
        if score >= 1:
            return 7 - score
        else:
            return 6
        return

    answer = []
    L = 0                       # 최저점
    for score in lottos:
        if score in win_nums:   # 일치하는 숫자를 발견하면 최저점 +1
            L += 1
    H = lottos.count(0) + L     # 최고점 = 최저점 + 0의 개수
    HR, LR = rank(H), rank(L)   # 최고순위, 최저순위
    
    return [HR, LR]