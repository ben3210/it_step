a, b, c = map(int, input("Enter three numbers (separate with space): ").split())
choice = int(input("Type numbers in bracket:\n(1) Minimum\n(2) Maximum\n(3) Arthimetic Mean\n"))

if choice == 1:
    minimum = min(a, b, c)
    print(f"Minimum: {minimum}")

elif choice == 2:
    maximum = max(a, b, c)
    print(f"Maximum: {maximum}")

elif choice == 3:
    mean = (a + b + c) / 3
    print(f"Mean: {mean}")

else:
    print("Invalid Input!")