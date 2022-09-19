N = int(input())
list_word = []

for i in range(N):
    word = input()
    list_word.append(word)
    
set_word = set(list_word)
list_word = list(set_word)

list_word.sort()
list_word.sort(key=len)

for i in list_word:
    print(i)