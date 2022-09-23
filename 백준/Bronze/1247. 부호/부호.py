for _ in range(3):
    T = int(input())
    num_list = [int(input()) for _ in range(T)]
    
    if sum(num_list) == 0:
        print(0)
    elif sum(num_list) > 0:
        print("+")
    else:
        print("-")
        