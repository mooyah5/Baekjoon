alphanets = 'abcdefghijklmnopqrstuvwxyz'
dict_alphabets = {}

for i in range(len(26)):
    dict_alphabets[alphanets[i]] = -1

S = input()

# list_S = list(map(str, S))
# list_num = [-1 for i in range(26)]
# print(list_num)
for i in range(len(S)):    
    for j in range(26):
        if S[i] == dict_alphabets[i]:
            

    # a~z 97~122