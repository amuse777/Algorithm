# https://www.acmicpc.net/problem/10866
# 덱, Silver4 (정답 비율 : 56%)


from collections import deque
import sys


class Deque:
    def __init__(self):
        self.len = 0
        self.deque = deque()

    def push_front(self, num):
        self.deque.appendleft(num)
        self.len += 1

    def push_back(self, num):
        self.deque.append(num)
        self.len += 1

    def pop_front(self):
        if self.len == 0: return -1
        else:
            self.len -= 1
            return self.deque.popleft()

    def pop_back(self):
        if self.len == 0: return -1
        else:
            self.len -= 1
            return self.deque.pop()

    def size(self):
        return self.len

    def empty(self):
        if self.len == 0: return 1
        else: return 0

    def front(self):
        if self.len == 0: return -1
        else: return self.deque[0]

    def back(self):
        if self.len == 0: return -1
        else: return self.deque[-1]


N = int(input())
Deque = Deque()

while N > 0:
    N -= 1
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front': Deque.push_front(cmd[1])
    elif cmd[0] == 'push_back': Deque.push_back(cmd[1])
    elif cmd[0] == 'pop_front': print(Deque.pop_front())
    elif cmd[0] == 'pop_back': print(Deque.pop_back())
    elif cmd[0] == 'size': print(Deque.size())
    elif cmd[0] == 'empty': print(Deque.empty())
    elif cmd[0] == 'front': print(Deque.front())
    elif cmd[0] == 'back': print(Deque.back())
