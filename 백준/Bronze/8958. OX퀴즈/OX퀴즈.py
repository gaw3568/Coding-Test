T_case = int(input())
for _ in range(T_case):
    test = input()
    sum_o = 0
    ing_o = 0
    
    for i in range(len(test)):
        if test[i] == 'X':
            ing_o = 0
        if test[i] == 'O':
            ing_o += 1
        sum_o += ing_o
            
    print(sum_o)
