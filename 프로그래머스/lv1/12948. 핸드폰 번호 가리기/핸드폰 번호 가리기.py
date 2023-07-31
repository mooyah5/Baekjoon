def solution(phone_number):
    answer = ''
    phone_number = phone_number[::-1]
    for i in range(len(phone_number)-1, -1, -1):
        if i >= 4:
            answer += '*'
        else:
            answer += phone_number[i]
    return answer