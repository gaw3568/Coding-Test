N = int(input())

number_list = []

for _ in range(N):
    num = int(input())
    number_list.append(num)
    
number_list.sort()

for number in number_list:
    print(number)