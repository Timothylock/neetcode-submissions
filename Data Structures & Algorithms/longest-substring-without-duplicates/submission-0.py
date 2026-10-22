class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        res = 0

        for i in range(len(s)):
            letter = s[i]
            if letter in seen:
                while letter in seen and l <= i:
                    seen.pop(s[l])
                    l += 1

            seen[letter] = True
            res = max(res, len(seen.keys()))
                    
        return res

        