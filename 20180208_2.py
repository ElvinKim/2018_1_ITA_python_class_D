while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        print("{} / {} = {}".format(a, b, a/b))
    except:
        print("미안")