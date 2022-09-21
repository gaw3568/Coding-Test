N = int(input())
start_num = 666
result = 0

while True:
    if '666' in str(start_num):
        result += 1
        if result == N:
            print(start_num)
            break
    start_num += 1