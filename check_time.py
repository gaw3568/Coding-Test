# 코딩 테스트 문제 시간 측정
# time.time() 이용
import time

start_time = time.time()

num1 = 20
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print(format(num1 / num2,".2f"))


end_time = time.time()

print("속도 측정 : ", format(end_time - start_time, ".2f"))
print("속도 측정 : ", round(end_time - start_time, 3))