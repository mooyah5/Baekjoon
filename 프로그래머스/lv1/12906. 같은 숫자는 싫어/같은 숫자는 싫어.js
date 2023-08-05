function solution(arr)
{
    const stack = [arr[0]]              // 스택에 첫번째 값만 넣어두고 시작!
    for (i=1; i< arr.length; i++) {     // 두번째 값부터 순회하면서, 이전 값과 다르면 스택에 삽입
        if (stack[stack.length-1] != arr[i]) {
            stack.push(arr[i])
        }
    }
    return stack;
}

//// 세트(Set)은 불가능하다.
// const set = Set(arr)는 다른 숫자 뒤에 다시 반복되는 숫자까지 사라져서 부적합

//// 하나씩 순회하면서 그 이전 값과 동일할 경우 pass 하는 방식을 사용했다.