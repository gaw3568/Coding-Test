def solution(num):
    num_count_one = bin(num)[2:].count("1")

    while num > 1:
        num += 1
        bin_num = bin(num)[2:]
        if bin_num.count("1") == num_count_one:
            return int(bin_num, 2)
            