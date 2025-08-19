def range_product(start, end):
    if start > end: start,end = end,start 
    product = 1
    for i in range(start, end+1): product *= i
    return f"product of integer numbers in range({start} - {end}):\033[91m {product}\033[0m"

print("Enter Range")
start = int(input("Start: "))
end = int(input("End: "))
print(range_product(start, end))