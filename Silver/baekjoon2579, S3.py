# https://www.acmicpc.net/problem/2579
# 계단 오르기, Silver3 (정답 비율 : 35%)

import sys

score = []
climb = []

N = int(input())
for _ in range(N):
    Num = int(sys.stdin.readline())
    score.append(Num)

if N == 1: print(score[0])
elif N == 2: print(max(score[1], score[0] + score[1]))
elif N == 3: print(max(score[0] + score[2], score[1] + score[2]))
else:
    climb.append(score[0])
    climb.append(max(score[1], score[0] + score[1]))
    climb.append(max(score[0] + score[2], score[1] + score[2]))
    for i in range(3, N):
        climb.append(max(climb[i - 3] + score[i - 1] + score[i],
                         climb[i - 2] + score[i]))

    print(climb[-1])

