def add_two_numbers() -> int:
    nums = input()
    nums_list = nums.split(',')
    nums_int = []
    for num in nums_list:
        nums_int.append(int(num))
    num_sum = sum(nums_int)
    return num_sum
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
