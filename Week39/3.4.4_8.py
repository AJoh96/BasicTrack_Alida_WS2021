while True:
    x = float(input("Length of side x"))
    y = float(input("Length of side y"))
    z = float(input("Length of hypotenuse"))
    if (x**2 + y**2) == (z**2):
        print("TRUE, The triangle is right-angled.")
    else:
        print("Wrong, the triangle is not right-angled.")