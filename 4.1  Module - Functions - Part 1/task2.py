def print_even(a, b):
    print(f"Even numbers in range {a} - {b}:")
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end=" ")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print_even(a, b)
