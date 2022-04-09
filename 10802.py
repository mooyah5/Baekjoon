# 문자열 분석
# 문자열 n(<= 100)개가 주어진다
# 각 문자열의 소문자, 대문자, 숫자, 공백 의 개수를 공백으로 구분하여 출력

while True:
    try:
        s = input()
        bin = 0
        upp = 0
        loww = 0
        num = 0
        for i in range(len(s)):
            if s[i] == ' ':
                bin += 1
            elif s[i].isupper():
                upp += 1
            elif s[i].islower():
                loww += 1
            elif s[i].isdecimal():
                num += 1
        print(loww, upp, num, bin)
    except EOFError :
        break