candy = int(input())

count = 0

for a in range(0, candy + 1):
    for b in range(0, candy + 1):
        for c in range(0, candy + 1):
            if a + b + c == candy:
                if a >= b + 2:
                    if a != 0 and b != 0 and c != 0:
                        if c % 2 == 0:
                            count += 1
print(count)                 