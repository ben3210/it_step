# #Sum
# def list_sum(nums):
#     sum = 0
#     for i in range(len(nums)):
#         sum += nums[i] 
#     return sum

# nums = [4, 56, 45, 6, 56, 0, -56]

# print("List:", nums)
# print("Sum: ", list_sum(nums))



list = [12, 23, 54, 89, 3]
def find_max(data):
    if len(data) == 1:
        return data[0]
    max_num = find_max(data[1:])
    if data[0] > max_num:
        return data[0]
    else:
        return max_num
    
print(find_max(list))