from typing import List

# 704. Binary Search
def search(nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) -1
        while min <= max:
            mid = (min + max) // 2
            number = nums[mid]
            if number == target:
                return mid
            elif number < target:
                min = mid + 1
            else:
                max = mid - 1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))