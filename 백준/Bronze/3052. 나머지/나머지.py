N = 10
rest_list = []

for _ in range(N):
    num = int(input())
    result = num % 42
    rest_list.append(result)

rest_set = set(rest_list)
print(len(rest_set))