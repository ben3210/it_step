#Monday 14 July 2025
def fib(num):
    series = []
    i = 0
    while i < num:
        if i < 2:
            series.append(i)
        else:
            series.append(series[-1] + series[-2])
        i += 1
    return series

num = int(input("Enter a number: "))
print(f"List of Fibonacci Sequence (range: 0 - {num}): \n", fib(num))