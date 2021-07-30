# https://www.acmicpc.net/problem/9012
# 괄호, Silver4 (정답 비율 : 42%)

# N = int(input())
#
# for _ in range(N):
#     M = input()
#     VPS = list(M)
#     num = 0
#
#     for i in VPS:
#         if i == '(': num += 1
#         elif i == ')': num -= 1
#         if num < 0:
#             print('NO')
#             break
#
#     if num > 0: print('NO')
#     elif num == 0: print('YES')

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