#Task Monday: 7 July WhatsApp Group

def check_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

def append_prime(function, n):
    if n < 2: 
        print("Invalid Input! (Enter a number greater than 1)")
        exit()
    prime = []
    for i in range(2, n+1):
        if function(i):
            prime.append(i)
    return f"List of Prime Numbers from 2 to {n}: \n{prime}\n"


n = int(input("\nEnter a number: "))
print(append_prime(check_prime, n))