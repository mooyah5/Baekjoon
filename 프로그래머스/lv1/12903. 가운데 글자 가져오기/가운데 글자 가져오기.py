def solution(s):
    idx = len(s) // 2
    if len(s) % 2:      # 홀수
        return s[idx]
    else:               # 짝수
        return s[idx-1:idx+1]