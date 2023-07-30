import collections
def solution(keymap, targets):
    answer = []
    key_dict = collections.defaultdict(int)
    for key in keymap:
        for i in range(len(key)):
            if key_dict[key[i]] > i+1 or key_dict[key[i]] == 0:
                key_dict[key[i]] = i+1
    # print(key_dict)        
    
    for target in targets:
        tmp = 0
        for t in target:
            if t not in key_dict:
                answer.append(-1)
                tmp = 0
                break
            else:
                tmp += key_dict[t]
        if len(answer) < len(targets) and tmp != 0:
            answer.append(tmp)
    return answer