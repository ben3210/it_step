num = 0
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

num = int(input("Enter a number (1 - 12): "))

if (num < 1) or (num > 12):
    print("Invalid Input!\n")

else:
    print(months[num], "\n")