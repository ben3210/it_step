while True:
    a, b = map(int, input("Enter two numbers: ").split())
    
    if a == 7 or b == 7:
        print("Goodbye!")
        break

    print("Sum: ", a+b)