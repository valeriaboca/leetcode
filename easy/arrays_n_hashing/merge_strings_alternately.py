
# 1768. Merge Strings Alternately
def mergeAlternately(word1: str, word2: str) -> str:
        i, j = 0, 0
        mergedString = []
        while i < len(word1) and j < len(word2):
            mergedString.append(word1[i])
            mergedString.append(word2[j])
            i += 1
            j += 1
        mergedString.append(word1[i:])
        mergedString.append(word2[j:])
        return "".join(mergedString)

word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))