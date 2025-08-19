while True:
    num = int(input("Enter a number: "))
    
    if num == 7:
        print("Goodbye!")
        break

    elif num > 0:
        print("Your Number is Positive")

    elif num < 0:
        print("Your Number is Negative")

    elif num == 0:
        print("Your Number is Equal to Zero")