# https://www.acmicpc.net/problem/10828
# 스택, Silver4 (정답 비율 : 38%)

import sys

# N = int(input())
# stack = []

# for _ in range(N):
#     cmd = sys.stdin.readline().split()
#     if cmd[0] == 'push':
#         stack.append(int(cmd[1]))
#
#     elif cmd[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())
#
#     elif cmd[0] == 'size':
#         print(len(stack))
#
#     elif cmd[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#
#     elif cmd[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

# ====================================================================
# Class Version

import sys


class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def pop(self):
        if self.len == 0: return -1
        else:
            self.len -= 1
            return self.list.pop()

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return -1 if self.len == 0 else self.list[-1]



N = int(input())
stack = Stack()

while N > 0:
    N -= 1
    command = sys.stdin.readline().split()

    if command[0] == 'push': stack.push(command[1])
    elif command[0] == 'pop': print(stack.pop())
    elif command[0] == 'size': print(stack.size())
    elif command[0] == 'empty': print(stack.empty())
    elif command[0] == 'top': print(stack.top())