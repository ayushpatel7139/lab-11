while True:
    try:
        int(input("enter number: "))
        print("valid")
        break
    except ValueError:
        print("invalid")
    
