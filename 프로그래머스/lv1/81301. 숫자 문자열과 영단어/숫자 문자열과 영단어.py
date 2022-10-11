def solution(s):
    num_eng = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    new_s = ""
    for index, num in enumerate(num_eng):
        if num in s:
            s = s.replace(num,str(index))
        new_s = s
    return int(new_s)