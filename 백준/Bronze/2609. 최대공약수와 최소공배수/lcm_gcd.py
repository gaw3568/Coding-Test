num1, num2 = map(int, input().split())
LCM = 0
GCD = 0

# 최소공배수
for i in range(max(num1,num2), (num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        LCM = i
        break

# 최대공약수

for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        GCD = i
        break

print(LCM)
print(GCD)