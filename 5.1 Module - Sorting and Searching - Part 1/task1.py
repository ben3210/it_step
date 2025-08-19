numbers = [2,64,3,0,5,5,100,-2]
n = len(numbers)
mean = sum(numbers) / n
sorted = False

first_two_thirds = n * 2 // 3
first_third = n // 3

if mean > 0:
    what_to_sort = first_two_thirds
else:
    what_to_sort = first_third

print(what_to_sort)
    
while not sorted:
    sorted = True
    for i in range(what_to_sort-1):
        if numbers[i] > numbers[i+1]:
            sorted = False
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
numbers[what_to_sort:] = numbers[:what_to_sort-1:-1]

print(numbers)