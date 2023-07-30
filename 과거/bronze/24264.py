# 알고리즘 수업 - 알고리즘의 수행 시간 3
# Bronze 3

# MenOfPassion 알고리즘

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# 코드1의 수행횟수와 최고차항의 차수를 출력

n = int(input())
print(n**2)
print(2)
