import sys
N = int(sys.stdin.readline().strip())
for _ in range(N):
    cnt = 0
    str = sys.stdin.readline().strip()
    
    for i in str:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
