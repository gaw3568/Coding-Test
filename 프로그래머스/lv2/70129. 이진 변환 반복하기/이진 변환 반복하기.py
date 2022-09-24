def solution(str_num):
    count_binary = 0
    count_zero = 0
    while True:
        if str_num == "1":
            return [count_binary,count_zero]
        count_zero += str_num.count("0")
        str_num = str_num.replace("0","")
        length = bin(len(str_num))[2:]
        str_num = str(length)
        count_binary += 1
