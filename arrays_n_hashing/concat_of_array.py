from typing import List

# 1929. Concatenation of Array
def getConcatenation(nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(n)
        return nums + ans

print(getConcatenation([1,2,1]))