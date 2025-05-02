from typing import List

# 1. Two Sum
# def twoSum(nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

# nums = [2,7,11,15]
# target = 9
# print(twoSum(nums, target))

# HashMap solution
def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))