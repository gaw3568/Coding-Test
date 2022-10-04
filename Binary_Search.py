import sys

def find_binary_search(num_list, find_num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == find_num:
            return mid
        
        if find_num < num_list[mid]:
            end = mid - 1
        elif find_num > num_list[mid]:
            start = mid + 1
        else:
            return None

N, find_num = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

result = find_binary_search(num_list, find_num, 0, N-1)

if result == None:
    print(f"해당 리스트 내에 숫자 {find_num}은 없음.")
else:
    print(f"해당 숫자 {find_num}의 위치는 배열 내 {result + 1}번째에 위치함.")
