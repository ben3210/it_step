a, b, c = map(int, input("Enter three numbers (separate with space): ").split())
operation = int(input("Type numbers in bracket:\n(1) Sum\n(2) Product\n"))

if operation == 1:
    sum = a + b + c
    print(f"{a} + {b} + {c} = {sum}")

elif operation == 2:
    product = a * b * c
    print(f"{a} * {b} * {c} = {product}")

else:
    print("Invalid Input!")