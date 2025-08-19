try:
    nums = []
    while True:        
        user = input("Enter a positive number or type 'quit' to finish: ")
        if user.lower() == "quit":
            break
        user = int(user)
        if user < 0:
            raise ValueError ("Negative Number is Entered!")
        nums.append(user)
    print(f"List: {nums} \nSum: {sum(nums)}")

except ValueError as ve:
    if "invalid literal" in str(ve): print("Error: Not a Number!")
    else: print(f"Error: {ve}")