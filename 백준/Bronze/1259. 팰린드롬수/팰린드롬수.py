while True:
    text = input()
    if text == '0':
        break
    
    if text == text[::-1]:
        print("yes")
    else:
        print("no")