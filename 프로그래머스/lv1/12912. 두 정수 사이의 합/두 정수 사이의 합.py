def solution(a, b):
    
    return ((a + b) * (b - a + 1) // 2 if a < b else (a + b) * (a - b + 1) // 2)