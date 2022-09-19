str_ = input().upper()
str_set = list(set(str_))
cnt_list = []

for i in str_set:
    cnt = str_.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
else:
    print(str_set[cnt_list.index(max(cnt_list))].upper())
