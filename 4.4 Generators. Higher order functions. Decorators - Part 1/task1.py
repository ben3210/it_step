def odd(start, end):
    for num in range(start, end+1):
        if num % 2 != 0:
            yield num

odd_nums = odd(0, 10)
for num in odd_nums:
    print(num)