import sys
student_list = []
N, K = map(int, sys.stdin.readline().split())
for _ in range(N):
	name, height = sys.stdin.readline().split()
	# height = float(height)
	student_list.append([name, height])
student_list.sort(key=lambda x: (x[0],float(x[1])))
print(f"{student_list[K-1][0]} {student_list[K-1][1]}")


"""
from functools import cmp_to_key
def cmp(a, b):
    if a[0] == b[0]:
        return a[1] < b[1]
    else:
        return a[0] < b[0]
arr = [] # [[string1, int1], [string2, int2], ...]
print(sorted(arr,key=cmp_to_key(cmp)))
"""
