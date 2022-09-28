def solution(s, n):
    new_s = list(s)
    for i in range(len(new_s)):
        if new_s[i].islower():
            new_s[i] = chr((ord(new_s[i]) - ord('a') + n) % 26  + ord('a'))
        elif new_s[i].isupper():
            new_s[i] = chr((ord(new_s[i]) - ord('A') + n) % 26  + ord('A'))
    return "".join(new_s)