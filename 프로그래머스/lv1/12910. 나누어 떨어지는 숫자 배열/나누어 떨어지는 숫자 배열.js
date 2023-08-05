function solution(arr, divisor) {
    var answer = [];
    // 1. 숫자 하나씩 순회하면서 나누어 떨어지면 answer Array에 삽입한다.
    for (a of arr) {
        if (a % divisor == 0) {
            answer.push(a)
        }
    }
    // 1-1. 예외: 나누어 떨어지는 요소가 없으면 -1만 담아 출력
    if (answer.length == 0) {
        return [-1]
    }
    // 2. answer Array를 오름차순으로 정렬
    answer.sort((a, b) => {
        return a-b
    })
    return answer;
}

//// .sort()

/// 1). default: 문자열
// 매개변수를 넣지 않으면 문자열로 인식하여 유니코드로 정렬한다.
// 예시로 [0, 1, 2, 10] 이라면, [0, 1, 10, 2] 이렇게 정렬된다.

/// 2) 숫자 정렬
// 매개변수에 인자 2개(a, b)를 받는 함수를 작성해야 한다.
// 해당 함수는 리턴하는 값이 양수일 때만 앞뒤를 바꾼다.
// 따라서 오름차순은 뒤에오는 숫자가 더 작을 때 음수가 되는 a-b, 내림차순은 a+b로 하면 된다.