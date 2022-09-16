n = int(input())
data = []

for i in range(n):
    data.append(int(input()))
    
data_new = sorted(data)

for i in range(len(data_new)):
    print(data_new[i])