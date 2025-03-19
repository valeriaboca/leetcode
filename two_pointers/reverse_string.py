from typing import List

# 344. Reverse String
def reverseString(s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

s = ["o","l","l","e","h"]
reverseString(s)
print(s)

# O(n) time : every element has to be read at least once
# O(1) time : modifies the list in place without creating a new one