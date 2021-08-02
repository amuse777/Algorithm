# https://www.acmicpc.net/problem/11050
# 이항 계수 1, Bronze1 (정답 비율 : 64%)


N, K = map(int, input().split())

def factorial(N):
    num = 1
    for i in range(2, N+1):
        num *= i
    return num

print(factorial(N) // (factorial(K) * factorial(N-K)))
