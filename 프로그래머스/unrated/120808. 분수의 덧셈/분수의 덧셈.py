def solution(denum1, num1, denum2, num2):
    denum_ = num1 * denum2 + num2 * denum1
    num_ = num1 * num2
    
    a = denum_
    b = num_
    if a < b:
        a, b = b, a
    
    while (a % b) != 0:
        tmp_num = a % b
        a = b
        b = tmp_num
    
    return [denum_ // b, num_ // b]