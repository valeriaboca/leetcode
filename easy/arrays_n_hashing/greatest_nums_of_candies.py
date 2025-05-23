from typing import List

# 1431. Kids With the Greatest Number of Candies
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= maxNum:
                result.append(True)
            else:
                result.append(False)
        return result

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))