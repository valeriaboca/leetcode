from typing import List

# 443. String Compression
def compress(chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            current_char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current_char:
                count += 1
                read += 1

            chars[write] = current_char
            write += 1

            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1

        return write

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))