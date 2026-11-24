from typing import List

def read_integers() -> List[int]:
    nums = input()
    nums_list = nums.split(',')
    nums_int = []
    for num in nums_list:
        nums_int.append(int(num))
    return nums_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
