def list_power(a, b):
    for i in range(len(a)):
        a[i] = a[i] ** b
    return a

nums = [2, 9, 14, 21, 33, 47]
power = 2

print("Initial List:", nums)
print(f"New List (Initial List to the power of {power}):\n", list_power(nums, power))
