def list_sum_v1(nums):
    print(f"\033[94mVersion 1:\n{'-' * 30}\033[0m")
    print(f"List: {nums} \nSum: {sum(nums)}")

def list_sum_v2(nums): 
    print(f"\033[94mVersion 2:\n{'-' * 30}\033[0m")
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

nums = []

#Version_1 Execution
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
    list_sum_v1(nums)
    
except ValueError as ve:
    if "invalid literal" in str(ve): print("Error: Not a Number!")
    else: print(f"Error: {ve}")

#Version_2 Execution - For my version getting input from user (not just fixed list), getting numbers from function is more safe
list_sum_v2(nums)

