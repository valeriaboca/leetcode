
from typing import List

def sortArray(nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
print(sortArray([5, 1, 1, 2, 0, 0]))