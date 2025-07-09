import sys
X = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

total_price = 0;

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    total_price += (a * b)
    
if total_price == X:
    print("Yes")
else:
    print("No")