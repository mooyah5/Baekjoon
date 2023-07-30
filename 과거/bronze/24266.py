# 알고리즘 수업 - 알고리즘의 수행 시간 5
# Bronze 3

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# 코드1의 수행횟수와 최고차항 (3이상이면 4)
n = int(input())
print(n**3)
print(3)
