from itertools import combinations

vowel = ['a','e','i','o','u']
l, c = map(int, input().split())
alphabet_list = input().split()
alphabet_list.sort()

for word in combinations(alphabet_list,l):
    vowel_cnt = 0

    for i in word:
        if i in vowel:
            vowel_cnt += 1

    if vowel_cnt >= 1 and len(word) - vowel_cnt >= 2:
        print("".join(word))
        
