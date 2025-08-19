def check_palindrome(num):

    #Checking if user input is a number
    try: n = int(num)
    except: print("\033[31mNot a number!\033[0m"); exit()

    reverse = num[::-1]
    if reverse == num: return f"{num} is a \033[34mPalindrome Number\033[0m"
    else: return f"{num} is \033[31mnot a Palindrome Number\033[0m"

num = input("Enter a number: ")
print(check_palindrome(num))