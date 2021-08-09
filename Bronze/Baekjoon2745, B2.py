# https://www.acmicpc.net/problem/2745
# 진법 변환, Bronze2 (정답 비율 : 56%)

import math

N, B = input().split()
B = int(B)
answer = 0
N = N[::-1]

for i in range(len(N)):
    if 'A' <= N[i] and N[i] <= 'Z': num = ord(N[i]) - 55
    else: num = int(N[i])
    answer += math.pow(B, i) * num

print(int(answer))


#===============================================================


# N, B = input().split()
# B = int(B)
# answer = 0
# N = N[::-1]
#
# A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for i in range(len(N)):
#     answer += A.index(N[i]) * (B ** i)
#
# print(int(answer))
