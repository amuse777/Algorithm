# https://www.acmicpc.net/problem/1159
# 농구 경기, Bronze2 (정답 비율 : 51%)

from collections import Counter

N = int(input())
name = []
first = []
cnt = 0

for i in range(N):
    M = input()
    name.append(M[0])
name_1 = Counter(name)
print(name_1)

for i, j in name_1.items():
    if j >= 5:
        first.append(i)
        cnt += 1
first.sort()

if cnt == 0: print('PREDAJA')
else: print(''.join(first))