
from typing import List

# 27. Remove Element
def removeElement(nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

print(removeElement([0,1,2,2,3,0,4,2], 2))