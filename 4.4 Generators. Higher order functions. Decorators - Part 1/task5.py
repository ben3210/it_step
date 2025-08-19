import time

def my_decorator(start, end):
    def actual_decorator(func):
        def wrapper():
            t1 = time.time()
            result = func(start, end)
            time_taken = time.time() - t1
            print(result)
            return f"\nTook {time_taken:.4f} seconds"
        return wrapper
    return actual_decorator

#@my_decorator
def print_even(start, end):
    even = []
    for num in range(start, end+1):
        if num % 2 == 0:
            even.append(num)
    return even

start = int(input("Start: "))
end = int(input("End: "))

print_even = my_decorator(start, end)(print_even)

print(print_even())