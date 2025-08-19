def summation(nums):
    return sum(nums)

def mean(nums):
    return sum(nums) / len(nums)

a, b = map(int, input("Enter two numbers (start - stop): ").split())

even = []
odd = []
multiples9 = []

for i in range(a, b+1, 1):
    if i % 2 == 0:
        even.append(i)
    if i % 2 != 0:
        odd.append(i)
    if i % 9 == 0:
        multiples9.append(i)

categories = [("Even", even), ("Odd", odd), ("Multiples of 9", multiples9)]

for name, values in categories:
    print(f"\n{name}: ", values)
    print("Sum = ", summation(values))
    print("Mean = ", mean(values))

