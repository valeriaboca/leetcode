
# 231. Power of Two
def isPowerOfTwo(n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return isPowerOfTwo(n // 2)

print(isPowerOfTwo(5))