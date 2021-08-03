# https://www.acmicpc.net/problem/9012
# 괄호, Silver4 (정답 비율 : 42%)

# import sys
#
# N = int(input())
#
# for _ in range(N):
#     M = list(sys.stdin.readline())
#     num = 0
#     answer = 0
#     for i in M:
#         if i == '(': num += 1
#         elif i == ')':
#             if num == 0:
#                 print('NO')
#                 answer += 1
#                 break
#             else:
#                 num -= 1
#
#     if num != 0 and answer == 0: print('NO')
#     elif num == 0 and answer == 0: print('YES')

#============================================================
# stack 활용

N = int(input())

for _ in range(N):
    stack = []
    M = input()
    VPS = list(M)
    cnt = 0

    for i in VPS:
        if i == '(': stack.append(i)

        else:
            if len(stack) == 0:
                print('NO')
                cnt = 1
                break
            else:
                stack.pop()

    if len(stack) != 0 and cnt == 0: print('NO')
    elif len(stack) == 0 and cnt == 0: print('YES')