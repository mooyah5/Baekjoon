# 0666
# 1666
# 2666
# 3666
# 4666
# 5666
# 6660
# 6661
# 6662
# 6663
# 6664
# 6665
# 6666
# 6667
# 6668
# 6669
# 7666
# 8666
# 9666
# 1 0666
# 1 1666

# 3자리 : 0666 => 1

# 4자리 : *666 (1~9), 666* (0~9) => 90

# 5자리 : **666 (1~9)(0~9), *666* (1~9)(0~9), 666** (0~9)(0~9) => 90+90+100 = 280

# 6자리 : ***666 (900), **666* (900), *666**(900), 666***(1000) => 270,000,000,000

n = int(input())

int6 = 666
cnt = 0

while True :
    if '666' in str(int6):
        cnt + 1
    if cnt == n:
        print(int6)
        break
    int6 += 1
print(int6)
