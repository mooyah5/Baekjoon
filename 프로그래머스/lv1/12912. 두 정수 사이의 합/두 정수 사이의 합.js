function solution(a, b) {
    var answer = 0;
    if (b > a) {
        tmp = b
        b = a
        a = tmp
    }
    for (i=b; i<=a; i++) {
        answer += i
    }
    return answer;
}