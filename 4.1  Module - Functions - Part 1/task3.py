def print_square(length, symbol, is_solid):
    if is_solid != "True" and is_solid != "False":
        print("Invalid Input! Hint: Type true/false")
        exit()

    is_solid = is_solid == "True" #converting string to boolean
    print("")

    if is_solid:
        for i in range(length):
            for j in range(length):
                print(symbol, end=" ")
            print("")

    else:
        for i in range(length):
            for j in range(length):
                if (i == 0 or i == length - 1) or (j == 0 or j == length - 1):
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")
            print("")

    print("")


print("Enter Details to Print Square")
length = int(input("Length: "))
symbol = input("Symbol: ")
is_solid = input("Solid or Empty(Type <True> or <False> respectively): ").capitalize()
print_square(length, symbol, is_solid)