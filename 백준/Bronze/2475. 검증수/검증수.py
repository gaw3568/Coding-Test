a, b, c, d, e = map(int, input().split())
verification_number = (pow(a,2) + pow(b,2) + pow(c,2) + pow(d,2) + pow(e,2)) % 10
print(verification_number)