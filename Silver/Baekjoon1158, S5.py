# https://www.acmicpc.net/problem/1158
# 요세푸스 문제, Silver5 (정답 비율 : 48%)
# 첫 deque 활용

from collections import deque

N, K = map(int, input().split())

num = deque([i for i in range(1, N+1)])
answer = []

while num:
    num.rotate(-(K-1))
    answer.append(str(num.popleft()))

print('<{0}>'.format(', '.join(answer)))