def solution(s):
    new_s = s.split(" ")
    for i in range(len(new_s)):
        new_s[i] = new_s[i].capitalize()
    return " ".join(new_s)