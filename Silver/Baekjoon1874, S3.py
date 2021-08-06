# https://www.acmicpc.net/problem/1874
# 스택 수열, Silver3 (정답 비율 : 34%)


N = int(input())
stack = []
answer = []
cnt = 1

for _ in range(N):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')

    else:
        print('NO')
        exit(0)

for i in answer:
    print(i)
