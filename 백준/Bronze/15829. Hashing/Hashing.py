L = int(input())
text = input().lower()
result = 0

for i in range(L):
    result += (ord(text[i])-96) * (31**i)
print(result % 1234567891)
