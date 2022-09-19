a = int(input())
b = int(input())
c = int(input())

count_list = [0,1,2,3,4,5,6,7,8,9]
multi_abc = str(a * b * c)

for i in count_list:
    print(multi_abc.count(str(i)))