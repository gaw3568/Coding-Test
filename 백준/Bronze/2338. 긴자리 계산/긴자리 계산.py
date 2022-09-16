a = int(input())
b = int(input())

print(a + b)
if (b < 0):
    n_b = abs(b)
    print(a + n_b)    
else:
    print(a - b)
print(a * b)