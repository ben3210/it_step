import time

def my_decorator(func):
    def wrapper():
        t1 = time.time()
        result = func()
        time_taken = time.time() - t1
        print(result)
        return f"\nTook {time_taken:.4f} seconds"
    return wrapper

@my_decorator
def print_even():
    even = []
    for num in range(100000+1):
        if num % 2 == 0:
            even.append(num)
    return even

#print_even = my_decorator(print_even)
print(print_even())