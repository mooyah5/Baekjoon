function solution(a, b) {
    var answer = '';
    const lst = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    let now = new Date(2016, a-1, b)
    return lst[now.getDay()];   // 요일별 분기처리할 필요 없이, 리스트에 일요일부터 순서대로 담아 높으면 요일 숫자를 인덱스처럼 활용할 수 있다. 0: 일, 1:월, ... , 6: 토
}

//// new Date(년, 월, 일)
// 년은 4자리로 입력한다 (두자리 입력 시 자동 1900년대)
// 월은 0부터 시작하므로 -1 처리 해준다.