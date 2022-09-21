from sys import stdin, stdout
N = stdin.readline()
A_list = set(stdin.readline().split())

M = stdin.readline()
B_list = stdin.readline().split()

for i in B_list:
    if i in A_list:
        stdout.write("1\n")
    else:
        stdout.write("0\n")