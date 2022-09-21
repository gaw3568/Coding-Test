N = int(input())
num_list = list(map(int, input().split()))
count = 0
more_divisor = 0

for x in num_list:
    for y in range(2,x):
        if x % y == 0:
            more_divisor += 1
            break
    if more_divisor == 0 and x != 1:
        count += 1
    more_divisor = 0
print(count)