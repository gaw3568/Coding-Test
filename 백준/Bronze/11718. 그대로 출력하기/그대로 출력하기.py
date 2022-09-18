while True:
    try:
        text = input()
        print(text)
    except EOFError:
        break
    