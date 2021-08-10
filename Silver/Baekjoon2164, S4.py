# https://www.acmicpc.net/problem/2164
# 카드2, Silver4 (정답 비율 : 53%)

import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque(i for i in range(1, N+1))

while len(card) > 1:
    card.popleft()
    card.rotate(-1)

print(card.pop())


# ====================================================

# 규칙을 살펴보자. n(입력값), a(결과값)
# (1, 1) / (2, 2) / (3, 2) (4, 4) / (5, 2) (6, 4) (7, 6) (8, 8) / (9, 2) ~ (16, 16)
# 입력값 1을 제외한 나머지 입력값은 2의 배수를 기준으로 결과값이 입력값과 같을 때까지 2의 배수로 증가한다.
# 같아진다면 다음 수를 기준으로 다시 2부터 배수로 결과값을 받게 된다.
# 그렇다면 공식은 (입력값 - 2**n) * 2가 된다.

n = int(input())
rem = n
cnt = 0

while rem > 1:
    rem //= 2
    cnt += 1

if n == 2**cnt: print(n)
else: print((n - 2**cnt) * 2)
