def great_user_v1(name, age):
    print("\033[94mVersion 1:\033[0m")
    age = int(age)
    if age < 0 or age > 130:
        raise ValueError ("Age out of range! \nHint: Age should be greater than 0 and less than 130")
    print(f"Hello \033[33m{name}\033[0m! Your age is \033[33m{age}\033[0m")
    
def great_user_v2(name, age):
    print("\033[94mVersion 2:\033[0m")
    try:
        age = int(age)
        if age < 0 or age > 130:
            raise ValueError ("Age out of range! \nHint: Age should be greater than 0 and less than 130")
        print(f"Hello \033[33m{name}\033[0m! Your age is \033[33m{age}\033[0m")
    except ValueError as ve:
        #checking whether age is out of range or is not a number: if not a number: ve as a string == 'invalid literal for int() with base 10: {age} ' 
        # else ve as string == "Age out of range! \nHint: Age should be greater than 0 and less than 130"
        if "invalid literal" in str(ve):
            print("Invalid Input! \nHint: Age should be a number")
        else:
            print(ve)

    
name = input("Name: ")
age = input("Age: ")

#try/except for version 1
try:
    great_user_v1(name, age)
    
except ValueError as ve:
    if "invalid literal" in str(ve):
        print("Invalid Input! \nHint: Age should be a number")
    else:
        print(ve)

#calling version 2 function
great_user_v2(name, age)

