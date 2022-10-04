import math
def solution(denum1, num1, denum2, num2):
    denum_ = num1 * denum2 + num2 * denum1
    num_ = num1 * num2
    gcd_num = math.gcd(denum_,num_)
    
    return [denum_ // gcd_num, num_ // gcd_num]