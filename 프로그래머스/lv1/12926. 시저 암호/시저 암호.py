def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        j = ord(s[i]) + n
        if s[i].isupper():  # 대문자 (65-90)
            if j > 90:
                j = 64 + ord(s[i]) + n - 90
        else:               # 소문자 (97-122)
            if j > 122:
                j = 96 + ord(s[i]) + n - 122
        answer += chr(j)
    return answer