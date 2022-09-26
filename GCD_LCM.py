# 유클리드 호제법을 적용한 풀이

"""
1. 최소공배수는 num1, num2를 곱한 값을 최대공약수로 나눈 값이다.
2. 최대공약수는 G(num1, num2) = G(num2, num1 % num2)의 형태가 가능하다.
"""
def GCD_LCM(num1, num2):
    if num1 < num2: 
        num1, num2 = num2, num1
    a = num1
    b = num2
    while (a % b) != 0:
        tmp_num = a % b
        a = b
        b = tmp_num
    
    return [b, int((num1*num2) / b)]


num1, num2 = map(int, input().split())

print(GCD_LCM(num1,num2))