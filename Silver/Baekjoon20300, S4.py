# https://www.acmicpc.net/problem/20300
# 서강근육맨, Silver4 (정답 비율 : 36%)

import sys

N = int(input())
M = list(map(int, sys.stdin.readline().split()))
M.sort()
MAX = 0

if N % 2 == 0:
    for i in range(N // 2):
        MAX = max(MAX, M[i] + M[N - 1 - i])

else:
    for i in range(N // 2):
        MAX = max(MAX, M[i] + M[N - 2 - i])
    MAX = max(MAX, M[-1])

print(MAX)
