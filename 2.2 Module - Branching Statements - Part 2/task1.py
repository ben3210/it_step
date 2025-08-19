num = 0
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

while num != 8:
    num = int(input("Enter a number (1 - 7)  (8: Quit): "))

    if num == 8:
        quit
    
    elif (num < 1) or (num > 8):
        print("Invalid Input! Try Again: \n")

    else:
        print(days[num], "\n")