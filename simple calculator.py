while True:
    a=input("Enter a number (or a letter to exit): ")
    try:
        int(a)
    except:
        print ("Program closed")
        break

    operations=("+", "-", "/", "*")
    func=input("Enter an operation: ")

    while func not in operations:
        print ("Please try again")
        func=input("Enter an operation: ")

    while True:
        b=input("Enter another number: ")
        try:
            int(b)
            break
        except:
            print ("Please try again")
            continue

    if func=="+":
        ans=int(a)+int(b)
        print (ans)

    if func=="-":
        ans=int(a)-int(b)
        print (ans)

    if func=="/":
        ans=int(a)/int(b)
        print (ans)

    if func=="*":
        ans=int(a)*int(b)
        print (ans)
