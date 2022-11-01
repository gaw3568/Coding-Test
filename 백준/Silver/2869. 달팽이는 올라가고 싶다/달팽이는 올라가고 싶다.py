import math
A, B, V = map(int, input().split())
goal_day = (V-B) / (A-B)

print(math.ceil(goal_day))