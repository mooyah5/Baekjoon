function solution(s) {
    if (s.length % 2 == 0) { 
        return s.substr(s.length/2 - 1, 2)
    } else { 
        return s.substr(s.length / 2, 1)
    }   
}

// str.substr(시작인덱스, 문자열 길이) : 문자열을 잘라주며, 소수점 이하는 자동으로 잘라준다.

// Math.floor() : 버림(몫)
// Math.ceil() : 올림
// Math.round() : 반올림