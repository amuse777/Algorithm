# https://www.acmicpc.net/problem/18511
# 큰 수 구성하기, Silver5 (정답 비율 : 28%)

import itertools

maximum, N = map(int, input().split())
len_max = len(str(maximum))

elements = list(map(int, input().split()))
elements.sort(reverse=True)
len_numbers = len(elements)
cnt = 0

while not cnt:
    case = list(itertools.product(elements, repeat=len_max))
    for i in case:
        num = ''.join(map(str, i))
        if maximum >= int(num):
            print(num)
            cnt = 1
            break

    len_max -= 1