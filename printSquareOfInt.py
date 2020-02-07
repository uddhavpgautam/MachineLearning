def squareOfIntOnly():
    flag, p1 = True, 0
    while flag:
        value = input("Provide anything to square value!")
        try:p1, flag = int(value), False
        except:print("Provide integer only!")
        else:print(p1*p1)
squareOfIntOnly()
