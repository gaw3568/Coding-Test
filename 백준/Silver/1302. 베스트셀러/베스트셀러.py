import sys

N = int(sys.stdin.readline())
book_list = dict()

for _ in range(N):
    book_name = sys.stdin.readline().strip().lower()

    if book_list.get(book_name) is None:
        book_list[book_name] = 1
    else:
        book_list[book_name] += 1

result = [name for name, sell_num in book_list.items() if max(book_list.values()) == sell_num]
print(sorted(result)[0])