# 재귀 함수

# 구현                재귀 함수
# 완전 탐색


# 3자리 7진수

# 00
# 01
# 02
# 10
# 11
# 12
# 20
# 21
# 22

# m = int(input())
# for i in range(m):
#     for j in range(m):
#         for k in range(m):
#             print(str(i) + str(j) + str(k))

# a = int(input())
# for i in range(a):
#     for j in range(a):
#         for k in range(a):
#             for l in range(a):
#                 print(f'{i} {j} {k} {l}')

# m = sc.nextInt();
# for(int i = 0; i < m; i++){
#     for(int j = 0; j < m; j++){
#         for(int k = 0; k < m; k++){
#           System.out.println(i + " " + j + " " + k);
#         }
#     }
# }

# n, m을 입력 받아서 n자리 m진수를 모두 출력해라

# n중 반복문 구현

# 3가지 템플릿
# 문제에 맞게 재귀 설계 X
# 문제를 우리가 가진 틀에 맞게 변형

# 2가지 템플릿 => 2차원 백트래킹

# 0-based

#1번 => n자리 m진수 모두 출력 => 순열

# n, m = map(int, input().split())

# arr = [0 for i in range(n)]
# def recur(cur):
#     if cur == n:
#         print(*arr)
#         return

#     for i in range(m):
#         arr[cur] = i
#         recur(cur + 1)
#         cnt += 1

# recur(0)


#오늘의 목표
# n자리 m진수의 3가지 방식을 배운다. => 외운다
# 문제를 n자리 m진수 문제로 변형하는 법을 배운다.

# 3 5


# 3 5



#2번 템플릿 => 한 케이스 내에 중복된 값이 없는 순열

# n, m = map(int, input().split()) # 3자리 4진수
# visited = [False for i in range(m)] #[t, f, f, f]

# arr = [0 for i in range(n)] # [0, 1, 2]
# def recur(cur): 
#     if cur == n: # cur += 1 ~ 자리수-1
#         print(*arr)
#         return

#     for i in range(m): #(진수) [0, 1, 2, 3]
#         if visited[i]:
#             continue

#         arr[cur] = i # 0
#         visited[i] = True
#         recur(cur + 1) # cur(2)
#             # for i in range(m): #(진수) [0, 1, 2, 3]
#             #     if visited[i]:
#             #         continue

#             #     arr[cur] = i # 0
#             #     visited[i] = True
#             #     recur(cur + 1) # cur(2)
#         visited[i] = False

# recur(0)




# 3번 템플릿 => 중복된 케이스를 안본다. => 조합

# 012

# 오름차순만 남긴다.
# 비내림차순

# n, m = map(int, input().split()) # 3 5
# # n, m = 2, 4
# arr = [0 for i in range(n)] # [0, 0, 0]

# def recur(cur, start):
#     if cur == n:
#         print(*arr)
#         return

#     for i in range(start, m): # [ 2, 3, 4]
#         arr[cur] = i # [0, 0, 0] [0, 1, 0] [0, 1, 2]
#         recur(cur + 1, i + 1) # 1, 1 # 2, 2

# recur(0, 0)

# n, m = map(int, input().split())



# arr = [0, 3]
# visited = [True, False, False, True, False]

# arr = [0, 3 5  6 ? ? ]
# visited = [True, False, False, True, False, True, True, False]

# public static void
# recur(int cur){
# if (cur == n)
# {
#   for (int i = 0; i < n; i++){
#     System.out.print(arr[i] + " ");
#   }
#   System.out.println("");
#
#   return;
# }
#
# for (int i = 0; i < m; i++){
#     if (visited[i]) continue;
#
#     arr[cur] = i;
#     visited[i] = true;
#     recur(cur + 1);
#     visited[i] = false;
# }
# }






# n = int(input())
# ineq = input().split()
# arr = [0 for i in range(n + 1)]
# visited = [False for i in range(10)]

# < >
# 0 2 1

# i => i, i + 1

# def recur(cur):
#     if cur == n + 1:
#         for i in range(n):
#             if ineq[i] == '<' and arr[i] > arr[i + 1]:
#                 return
#             if ineq[i] == '>' and arr[i] < arr[i + 1]:
#                 return

#         print(*arr)
#         return

#     for i in range(10)[::-1]:
#         if visited[i]:
#             continue

#         arr[cur] = i
#         visited[i] = True
#         recur(cur + 1)
#         visited[i] = False

# recur(0)