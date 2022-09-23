def solution(n):
    subak = "수박"
    if n % 2 == 0:
        return subak * (n//2)
    else:
        return subak * (n//2) + "수"