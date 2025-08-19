def digits_number(num):

    #Checking if user input is a number
    try: n = int(num)
    except: print("\033[31mNot a number!\033[0m"); exit()

    return f"Length of \033[34m{num}\033[0m: {len(num)}"    
    

num = input("Enter a number: ")
print(digits_number(num))