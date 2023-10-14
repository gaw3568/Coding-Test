T = int(input())

for _ in range(T):
    list_a = []
    check_str = input()

    for ch in check_str:
        if ch == '(':
            list_a.append(ch)
        else:
            if not list_a:
                list_a.append(ch)
                break
            list_a.pop()

    if list_a:
        print("NO")
    else:
        print("YES")
