# N의 약수의 총 합 구하기

# 방법 1
def sumDivisor(num):
    # num / 2 의 숫자만 num의 약수인지 검사한 후, 마지막에 num을 더해주고
    # num의 약수의 합 return
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# 방법2
def getMyDivisor(n):
    divisors_list = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisors_list.append(i) 
            if ( (i**2) != n) : 
                divisors_list.append(n // i)
    # divisors_list.sort()
    return sum(divisors_list)

# main
N = int(input())
print(f"{N}의 약수의 합은 {sumDivisor(N)}")
print(f"{N}의 약수의 합은 {getMyDivisor(N)}")

