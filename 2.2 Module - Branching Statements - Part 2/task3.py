#using try/except to catch error of a non numerical input
try: 
    num = int(input("Enter a number: "))

except:
    print("Invalid Input. That's not a number!")
    exit()

if num > 0:
    print("Your number is Positive")

elif num < 0:
    print("Your number is Negative")

else:
    print("Your number is equal to zero")