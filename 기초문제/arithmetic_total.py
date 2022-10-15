from math import ceil, fabs, fsum

# 두 정수를 이용한 합, 차, 곱, 몫, 나머지, 나눈 값(소수점 둘째 자리까지 나타냄) 출력
num1, num2 = map(int, input().split())
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print(format(num1 / num2,".2f"))

# math 클래스의 여러 함수를 사용하는 방법

print(ceil(1.2))   # 반올림
print(fabs(-1.2))  # Floating abs
print(fsum([1,2,3,4,5,6,7]))    # Float sum
