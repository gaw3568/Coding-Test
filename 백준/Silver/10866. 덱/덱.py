import sys
from collections import deque
N = int(sys.stdin.readline().strip())
stack = deque()
for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if "push_front" in cmd:
        cmd = cmd.split()
        stack.appendleft(int(cmd[-1]))
    elif "push_back" in cmd:
        cmd = cmd.split()
        stack.append(int(cmd[-1]))
    elif cmd == "pop_front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())
    elif cmd == "pop_back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif cmd == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])