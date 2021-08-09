# https://www.acmicpc.net/problem/21313
# 문어, Bronze2 (정답 비율 : 75%)\


N = int(input())

if N % 2 == 0:
    result = [1, 2] * (N//2)
    print(*result)

else:
    result = [1, 2] * (N//2) + [3]
    print(*result)