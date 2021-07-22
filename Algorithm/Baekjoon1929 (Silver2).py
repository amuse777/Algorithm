# https://www.acmicpc.net/problem/1929
# 소수 구하기 (정답 비율 : 27%)
# 에라토스테네스의 체를 이용

import math

M, N = map(int, input().split())


def prime(N):
    sieve = [True] * (N + 1)

    # 1, 2, 3은 아래 for 문장에 해당되지 않으므로 return 문장에 있는 for 문장으로 간다.
    for i in range(2, int(math.sqrt(N)) + 1):
        if sieve[i] == True:
            for j in range(i + i, N + 1, i):
                sieve[j] = False

    # 5, 7과 같은 문장은 위에서 'False' 선언이 되지 않았기 때문에 'True' 선언이 된다.
    return [i for i in range(M, N + 1) if sieve[i] == True]


answer = prime(N)
if 1 in answer: answer.remove(1)    # 1은 소수에 해당하지 않으므로 삭제
for i in answer:
    print(i)