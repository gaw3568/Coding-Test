T_case = int(input())
member_list = []
for _ in range(T_case):
    age, name = input().split()
    member_list.append([age,name])

member_list.sort(key = lambda x : int(x[0]))

for i in range(T_case):
    print(member_list[i][0], member_list[i][1])