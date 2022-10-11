def solution(sizes):
    size_1 = max([max(x) for x in sizes])
    size_2 = max([min(x) for x in sizes])
    return size_1 * size_2