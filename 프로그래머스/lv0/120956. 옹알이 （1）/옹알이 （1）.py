def solution(babbling):
    answer = 0
    pos = ['aya', 'ye', 'woo', 'ma']
    for bab in babbling:
        new = bab
        i = 0
        while len(bab) > i:
            for p in pos:
                if p in new:
                    new = new.replace(p, ' ')
                    i += len(p)
            else:
                i += 1
        if new.strip(' ') == '':
            answer += 1
    return answer