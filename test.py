for i in range(51):
    if i % 4 == 0:
        if i % 7 == 0:
            print("DerDor")
        else:
            print("Der")
    elif i % 7 == 0:
        print("Dor")
    else:
        print(i)