def solution(s):
    answer = 0      # 정답 개수
    start = ''      # 첫 글자
    a, b = 0, 0     # a=첫 글자 개수, b=다른 글자 개수
    for i in range(len(s)):
        # 첫글자는 start에 저장하고, a + 1
        if len(start) == 0:
            start = s[i]
            a += 1
        else:   # 첫글자와 같으면 a+1, 다른글자면 b+1
            if start == s[i]:
                a += 1
            else:
                b += 1
                
        # 두 횟수가 같아지는 순간 정답 개수를 +1 해주고, 상태값들을 초기화한다.
        if a == b:
            answer += 1
            a = 0
            b = 0
            start = ''
        # 두 횟수는 다르지만, 마지막 글자를 만난 경우에도 정답 개수를 올려준다.
        elif a != b and i == len(s)-1:
            answer += 1
    return answer