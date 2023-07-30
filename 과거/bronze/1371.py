# 가장 많은 글자

# 어떤 문장이 주어졌을 때, 가장 많이 나온 글자 출력

import sys
list_ = []
while True:
    try:
        list_.append(list(input()))
    except EOFError:
        break
print(list_)