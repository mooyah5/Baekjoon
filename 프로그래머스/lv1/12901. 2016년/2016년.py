import datetime
def solution(a, b):
    weeks = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    d = datetime.date(2016, a, b)
    return weeks[d.weekday()]