def solution(s):
    a_list = ""
    new_s = s.split(" ")
    for i in new_s:
        for x in range(len(i)):
            if x % 2 == 0:
                a_list += i[x].upper()
            else:
                a_list += i[x].lower()
        a_list += " "
    return a_list[:-1]