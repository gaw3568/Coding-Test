T_case = int(input())

for _ in range(T_case):
    r, text = input().split()
    str_new = ""
    for _ in range(len(text)):
        str_new += (int(r) * text[_])
    print(str_new)
