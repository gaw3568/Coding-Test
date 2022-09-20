import sys
from collections import Counter

N = int(sys.stdin.readline())
number_list = []

for i in range(N):
    number_list.append(int(sys.stdin.readline()))
number_list.sort()

print(round(sum(number_list) / N))
print(number_list[N // 2])

freq_list = Counter(number_list).most_common()
if len(freq_list) > 1 and freq_list[0][1] == freq_list[1][1]:
    print(freq_list[1][0])
else:
    print(freq_list[0][0])
print(number_list[-1] - number_list[0])