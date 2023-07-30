# 애너그램

# 소문자로 이루어진 단어가 주어진다.
# 길이는 20이하, 애너그램 수가 10만개 이하인 단어만 주어짐

# 단어 내 몇 철자가 중복될 수 있어, 같은 단어가 여러 번 만들어질 수 있는데,
# 단 한번씩만 출력해야 한다.

# 모든 애너그램 단어를 중복 없이 출력하셈


def anagrams(alpha: dict, l: int, s: str):  # alpha, 문자길이, 답
    if len(s) == l:
        string_set.add(s)
        return
    for al in alpha:
        if alpha[al]:
            alpha[al] -= 1  # al 사용처리
            s += al  # s 뒤에 al 붙이기
            anagrams(alpha, l, s)
            alpha[al] += 1  # al 사용 취소
            s = s[:-1]  # s 뒤에 al 빼기 (다른 al 탐색 위해)
    return


n = int(input())

for _ in range(n):
    string_set = set()  # 답들의 중복제거
    string = input()
    alpha = {}

    # alpha 딕셔너리에 {string의 각 문자: 0, ...} 채우기
    for s in string:
        if s in alpha:
            alpha[s] += 1
        else:
            alpha[s] = 1

    anagrams(alpha, len(string), "")
    string_set = sorted(list(string_set))  # set => list 그리고 알파벳순 정렬

    for s in string_set:
        print(s)
