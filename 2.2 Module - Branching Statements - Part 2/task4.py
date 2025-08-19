num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 == num2:
    print(f"{num1} = {num2}")

elif num2 < num1:
    print("Ascending order:", num2, num1)

else:
    print("Ascending order:", num1, num2)