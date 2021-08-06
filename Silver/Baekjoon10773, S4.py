# https://www.acmicpc.net/problem/10773
# 제로, Silver4 (정답 비율 : 67%)


K = int(input())
answer = []

for _ in range(K):
    N = int(input())
    if N == 0:
        answer.pop()
    else:
        answer.append(N)

print(sum(answer))