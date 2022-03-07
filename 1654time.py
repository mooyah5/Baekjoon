k, N = map(int, input().split())
lan_list = []
for i in range(k):
    lan_list.append(int(input()))

max_lan = sum(lan_list)/N #최대 길이
min_lan = 1

while mid_lan>= 1:
    quotient = 0
    mid_lan = (max_lan+min_lan)/2
    for i in lan_list:
        quotient += i // mid_lan
    if quotient > N:
        min_lan = mid_lan + 1 #몫이 n값보다 많으면 최솟값에 중간+1을 넣어줌
    else:
        max_lan = mid_lan - 1 #몫이 n값보다 작거나 같으면 최댓값에 중간-1을 (왜?)
