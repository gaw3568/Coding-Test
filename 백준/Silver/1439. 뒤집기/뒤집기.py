str_binary_num = input()

total_result = 0

for i in range(len(str_binary_num)-1):
    if str_binary_num[i] != str_binary_num[i+1]:
        total_result += 1

print((total_result + 1) // 2)