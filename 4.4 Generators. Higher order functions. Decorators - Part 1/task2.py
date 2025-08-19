numbers = [23, 87, 14, 56, 3, 78, 91, 45, 62, 10]

def out_of_range(lst, start, end):
    for num in lst:
        if num < start or num > end:
            yield num

start = int(input("Start: "))
end = int(input("End: "))
nums_out_of_range = out_of_range(numbers, start, end)

for i in nums_out_of_range:
    print(i)