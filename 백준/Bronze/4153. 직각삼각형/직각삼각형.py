while True:
    x_y_z = list(map(int, input().split()))

    if x_y_z.count(0) == 3:
        break
    x_y_z.sort()

    x_plus_y = x_y_z[0] + x_y_z[1]
    result = x_y_z[0]**2 + x_y_z[1]**2

    if (result == (x_y_z[2]**2)) and (x_plus_y > x_y_z[2]):
        print("right")
    else:
        print("wrong")