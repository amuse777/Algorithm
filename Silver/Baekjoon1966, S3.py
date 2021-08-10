# https://www.acmicpc.net/problem/1966
# 프린터 큐, Silver3 (정답 비율 : 55%)


from collections import deque

case = int(input())

for _ in range(case):
    N, M = map(int, input().split())

    test = deque(list(map(int, input().split())))
    test2 = deque([False] * N)
    test2[M] = True
    cnt = 0

    while True:
        if test[0] == max(test):
            cnt += 1

            if test2[0] == True:
                print(cnt)
                break
            else:
                test.popleft()
                test2.popleft()

        else:
            test.rotate(-1)
            test2.rotate(-1)
