def smallest(a, b, c, d, e):
    return min(a, b, c, d, e)

a, b, c, d, e = map(int, input("Enter 5 numbers (Separated by single space):\n").split())
print("Smalllest: ", smallest(a, b, c, d, e))