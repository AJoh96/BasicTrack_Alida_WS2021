while True:
    mark = float(input("What exam mark is it?"))
    if mark >= 75:
        print("First")
    elif mark < 75 and mark >=70:
        print("Upper second")
    elif mark < 70 and mark >=60:
        print("Second")
    elif mark < 60 and mark >=50:
        print("Third")
    elif mark < 50 and mark >=45:
        print("F1 Supp")
    elif mark < 45 and mark >=40:
        print("F2")
    elif mark < 40:
        print("F3")
    else:
        break
