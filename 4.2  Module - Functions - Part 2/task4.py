# Remove elements from list
def list_remove(nums):
    count = 0
    user = ""
    while True:
        user = input("Do you want to remove a number from the List?\nIf Yes <write the number>. If No type <no>\n")
        #try and except to 1. distinguish numerical input and words. 2. Detect Numbers not in list
        try:
            user = int(user)
            nums.remove(user)
            count += 1
        except:
            if user == "no": break
            print("Invalid Input!")
    return count


nums = [321 , 33, 7, 0, -12, 5 , 7, 1, 1000]

print("Initial List: ", nums)
n = list_remove(nums)
print("Final List: ", nums)
print("Number of elements removed:", n)