n = int(input())
dict_ = {}
for _ in range(n):
    name, do = map(str, input().split())
    if do == "enter":
        dict_[name] = 1
    else:
        del dict_[name]
new_dict = sorted(dict_.keys(), reverse=True)
print("\n".join(new_dict))