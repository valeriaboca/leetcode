
# 2390. Removing Stars from a String
def removeStars(s: str) -> str:
        arr = []
        for i in range(len(s)):
            if s[i] == '*':
                if arr: 
                    arr.pop()
            else:
                arr.append(s[i])
        return "".join(arr)

s = "leet**cod*e"
print(removeStars(s))