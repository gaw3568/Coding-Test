from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
stack = deque()
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if "push" in cmd:
        cmd = cmd.split()
        stack.append(int(cmd[-1]))
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())
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