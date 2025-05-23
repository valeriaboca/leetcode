from typing import List

# 26. Remove Duplicates from Sorted Array
def removeDuplicates( nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
print(removeDuplicates([1,1,2,3,4,4]))