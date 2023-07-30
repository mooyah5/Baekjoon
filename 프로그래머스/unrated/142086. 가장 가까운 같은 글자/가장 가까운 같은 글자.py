def solution(s):
    answer = []
    dct = dict()
    for i in range(len(s)):
        if s[i] not in dct: # 첫 문자면, res에 -1 추가
            answer.append(-1)
        else:   # 이미 등장한 문자면, res에 (현재 인덱스 - 이전 인덱스) 추가
            answer.append(i - dct[s[i]])
        dct[s[i]] = i   # 딕셔너리에 {현재 문자: 현재 인덱스} 추가
    return answer