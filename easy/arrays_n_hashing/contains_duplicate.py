from typing import List

# 217. Contains Duplicate
def containsDuplicate(nums: List[int]) -> bool:
        seen = set()
        for number in nums:
            if number in seen:
                return True
            seen.add(number)
        return False

print(containsDuplicate([1,2,3,1]))