def solution(sides):
    sides.sort()
    return 1 if sides[2] < (sides[0] + sides[1]) else 2
