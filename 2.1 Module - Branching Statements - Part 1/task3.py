meters = int(input("Enter number in meters: "))
choice = int(input("Type numbers in bracket:\n(1) Miles\n(2) Inches\n(3) Yards\n"))

if choice == 1:
    miles = meters / 1609.344
    print(f"{meters} meters = {miles} miles")

elif choice == 2:
    inches = meters * 39.3701
    print(f"{meters} meters = {inches} inches")

elif choice == 3:
    yards = meters * 1.09361
    print(f"{meters} meters = {yards} yards")

else:
    print("Invalid Input!")