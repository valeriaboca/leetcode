
# 242. Valid Anagram
def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s, freq_t = {}, {}

        for char in range(len(s)):
            freq_s[s[char]] = freq_s.get(s[char], 0) + 1
            freq_t[t[char]] = freq_t.get(t[char], 0) + 1
        return freq_t == freq_s

print(isAnagram(s='triangle', t='integral'))