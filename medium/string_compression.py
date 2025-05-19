from typing import List

# 443. String Compression
def compress(chars: List[str]) -> int:
        i, result = 0, 0

        while i < len(chars):
            curr_char = chars[i]
            occur = 0

            while (i < len(chars)) and (chars[i] == curr_char):
                occur += 1
                i += 1

            chars[result] = curr_char
            result += 1

            if occur > 1:
                occurStr = str(occur)

                for j in range(len(occurStr)):
                    chars[result] = occurStr[j]
                    result += 1

        return result

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))