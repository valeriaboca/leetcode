
# 374. Guess Number Higher or Lower
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber( n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                low = mid + 1
            else:
                high = mid - 1
        return low

pick = 7

print(guessNumber(10))