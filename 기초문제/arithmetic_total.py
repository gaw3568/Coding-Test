# 두 정수를 이용한 합, 차, 곱, 몫, 나머지, 나눈 값(소수점 둘째 자리까지 나타냄) 출력

num1, num2 = map(int, input().split())
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print(format(num1 / num2,".2f"))
