num_list = []

for _ in range(5):
    num = int(input())
    num_list.append(num)
    
num_list.sort()
    
average = int(sum(num_list) / len(num_list))
print(average)
print(num_list[2])