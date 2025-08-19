#Product
def list_product(nums):
    product = 1
    for i in range(len(nums)):
        product *= nums[i] 
    return product

n = int(input("Creating a List:\nHow many elements do you want to add? "))
nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

print("List:", nums)
print("Product: ", list_product(nums))

