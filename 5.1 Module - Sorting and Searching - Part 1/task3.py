def advanced_bubble_sort(lst):
    num_of_swaps = 1
    while num_of_swaps != 0:
        num_of_swaps = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                num_of_swaps += 1
                lst[i], lst[i+1] = lst[i+1], lst[i]
        #print(num_of_swaps)
    return lst

numbers = [23,7,3,0,5,8,4,3]
print(advanced_bubble_sort(numbers))