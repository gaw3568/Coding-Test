list_num = []
for _ in range(9):
    num = int(input())
    list_num.append(num)
print(max(list_num), list_num.index(max(list_num))+1)
