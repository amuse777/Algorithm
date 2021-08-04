# https://www.acmicpc.net/problem/3040
# 백설 공주와 일곱 난쟁이, Bronze2 (정답 비율 : 71%)


import itertools

num = []
result = []

for i in range(9):
    N = int(input())
    num.append(N)

num_result = list(itertools.combinations(num, 7))

for i in num_result:
    if sum(i) == 100:
        for j in i:
            print(j)