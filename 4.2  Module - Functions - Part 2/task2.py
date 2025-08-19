#Minimum
def list_min(nums):
    return min(nums)

n = int(input("Creating a List:\nHow many elements do you want to add? "))
nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

print("List:", nums)
print("Minimum: ", list_min(nums))