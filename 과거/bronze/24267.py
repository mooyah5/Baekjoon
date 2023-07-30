# 알고리즘 수업 - 알고리즘의 수행 시간 5
# Bronze 3

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# 코드1의 수행횟수와 최고차항 (3이상이면 4)

n = int(input())
print(n*(n-1)*(n-2)//6)
print(3)
