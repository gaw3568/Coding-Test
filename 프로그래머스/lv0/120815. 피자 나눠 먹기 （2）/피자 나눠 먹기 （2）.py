from math import gcd
def solution(n):
    return (n * 6) // gcd(n,6) // 6