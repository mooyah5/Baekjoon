function solution(n)
{
    var answer = 0;
    const new_n = n.toString()
    for (n of new_n) {
        answer += Number(n)
    }
    return answer;
}